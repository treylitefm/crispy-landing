from django.views.decorators.csrf import csrf_exempt

from models import Test
from ..launchpad.models import Page
from django.http import JsonResponse
import requests

MONITOR_RUNNER_URL = 'monitor:6000/'
BROWSERS = {
    'firefox': 0,
    'chrome': 1
}

def index(request, test_id):
    test = Test.objects.filter(id=test_id)
    
    if test:
        res = {}
        res['id'] = test.id
        res['status'] = test.status
        res['created_on'] = test.created_on
        res['updated_on'] = test.updated_on
        res['page_id'] = test.page.id
    else:
        res = False
        
    return JsonResponse({ 'test': res })

@csrf_exempt
def new_test(request, page_id):
    data = {}
    if request.method == 'POST':
        data = {}
        page = Page.objects.get(id=page_id)
        if 'browser' in request.POST:
            data['browser'] = request.POST['browser'].lower()
        else:
            data['browser'] = 'firefox'

        print data
        print request.POST

        test = Test.objects.create(page=page, status=0, browser=BROWSERS[data['browser']]) 
        test.save()
        domain = page.app.domain if page.app.domain[-1] != '/' else page.app.domain[:-1]
        data['url'] = page.app.get_protocol_display()+'://'+domain+page.path
        data['page_id'] = page.id
        data['app_id'] = page.app.id
        data['test_id'] = test.id

        requests.post(MONITOR_RUNNER_URL+'launch/', data)     
        data['status'] = 'QUEUED'

    return  JsonResponse({'data': data})

@csrf_exempt
def update_test(request, test_id):
    if request.method == 'POST':
        test = Test.objects.filter(id=test_id)
        if test:
            if 'screenshot' in request.POST:
                test.update(status=request.POST['status'], screenshot=request.POST['screenshot'])
            else:
                test.update(status=request.POST['status'])
    return JsonResponse({ 'test': ''})

@csrf_exempt
def get_tests(request, page_id):
    test_objects = Test.objects.filter(page__id=page_id)

    if test_objects:
        tests = [ (test.id, test.screenshot,test.created_on,) for test in test_objects ]
    else:
        tests = []
    return JsonResponse({
        'page_id': page_id,
        'tests': tests
    })
