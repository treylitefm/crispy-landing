from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from models import App,Page
from forms import AppForm,PageForm

def index(request):
    context = {
        'apps': App.objects.filter(owner__id=request.user.id),
        'status': {
            0: 'orange',
            1: 'yellow',
            2: 'green',
            3: 'red',
            4: 'error'
        },
    }

    return render(request, 'launchpad/index.html', context)

def new_app(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            app = form.save()
            return redirect(reverse('launchpad:show_app', kwargs={'app_id': app.id}))
    else:
        form = AppForm()

    return render(request, 'launchpad/new_app.html', {'form': form})

def show_app(request, app_id):
    app = App.objects.get(id=app_id)
    if app.page_set.all():
        thumbs = app.page_set.all().latest().test_set.all()
    else:
        thumbs = ''
    context = {
        'app': app,
        'form': PageForm(),
        'status': {
            0: 'orange',
            1: 'yellow',
            2: 'green',
            3: 'red',
            4: 'error'
        },
        'thumbs': thumbs
    }
    return render(request, 'launchpad/show_app.html', context)

def new_page(request, app_id):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid() and not Page.objects.filter(app__id=app_id).filter(path=form.cleaned_data['path']):
            page = form.save(commit=False)
            page.app = App.objects.get(id=app_id)
            page = form.save()
            return redirect(reverse('launchpad:show_app', kwargs={'app_id': app_id}))
    return redirect(reverse('launchpad:show_app', kwargs={'app_id': app_id}))

def show_page(request, app_id, page_id):
    app = App.objects.get(id=app_id)
    page = Page.objects.get(id=page_id)
    thumbs = page.test_set.all()

    context = {
        'app': app,
        'form': PageForm(),
        'status': {
            0: 'orange',
            1: 'yellow',
            2: 'green',
            3: 'red',
            4: 'error'
        },
        'thumbs': thumbs
    }
    return render(request, 'launchpad/show_app.html', context)

def edit_page(request, page_id):
    if 'enabled' in request.POST:
        enabled = request.POST['enabled'].lower()
        if enabled in ['true']:
            enabled = True
        elif enabled in ['false']:
            enabled = False
        page = Page.objects.filter(id=page_id)
        if page:
            print enabled,'yooo'
            page.update(enabled=enabled)

    return JsonResponse({
        'success': True    
    })
