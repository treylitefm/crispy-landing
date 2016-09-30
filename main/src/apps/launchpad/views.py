from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from models import App,Page
from forms import AppForm,PageForm

def index(request):
    context = {
        'apps': App.objects.filter(owner__id=request.user.id)
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
    context = {
        'app': App.objects.get(id=app_id),
        'form': PageForm()
    }
    return render(request, 'launchpad/show_app.html', context)

def new_page(request, app_id):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid() and not Page.objects.filter(path=form.cleaned_data['path']):
            page = form.save(commit=False)
            page.app = App.objects.get(id=app_id)
            page = form.save()
            return redirect(reverse('launchpad:show_app', kwargs={'app_id': app_id}))
    return redirect(reverse('launchpad:show_app', kwargs={'app_id': app_id}))

def show_page(request, page_id):
    return render(request, 'launchpad/show_page.html', context)
