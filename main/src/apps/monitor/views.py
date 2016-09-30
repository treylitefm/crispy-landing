from django.views.decorators.csrf import csrf_exempt

from models import Test
from ..launchpad.models import Page
from django.http import JsonResponse
import requests

MONITOR_RUNNER_URL = 'http://192.168.99.100:6000/'

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
        test = Test.objects.create(page=page, status=0) 
        test.save()
        domain = page.app.domain if page.app.domain[-1] != '/' else page.app.domain[:-1]
        data['url'] = page.app.get_protocol_display()+'://'+domain+page.path
        data['page_id'] = page.id
        data['app_id'] = page.app.id
        data['test_id'] = test.id
        if 'browser' in request.POST:
            data['browser'] = request.POST['browser']

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
