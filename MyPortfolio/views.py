from django.shortcuts import render
from publications.models import publication


def home(request):
    return render(request, 'home.html')

def programmimg(request):
    return render(request, 'programmimg.html')

def education(request):
    return render(request, 'education.html')

def add_info(request):
    pubs = publication.objects
    return render(request, 'add_info.html', {'pubs':pubs})            
