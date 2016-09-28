from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from models import App,Page
from forms import AppForm

def index(request):
    context = {
        'apps': App.objects.filter(owner__id=request.user.id)
    }

    print context['apps']
    print len(context['apps'])

    return render(request, 'launchpad/index.html', context)

def new_app(request):
    if request.method == 'POST':
        print request.POST
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('launchpad:new_page')
    else:
        form = AppForm()

    return render(request, 'launchpad/new_app.html', {'form': form})

def show_app(request, app_id):
    context = {
        'pages': ''
    }
    return render(request, 'launchpad/show_app.html', context)

def new_page(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            return redirect('launchpad:new_page')
    else:
        form = AppForm()
    return render(request, 'launchpad/new_page.html', {'form': form})

def show_page(request, page_id):
    return render(request, 'launchpad/show_page.html', context)
