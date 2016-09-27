from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'launchpad/index.html')

def show_app(request, app_id):
    return render(request, 'launchpad/app_summary.html')

def show_page(request, page_id):
    return render(request, 'launchpad/page_summary.html')
