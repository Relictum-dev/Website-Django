from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    return render(request, 'main/skills.html')

def works(request):
    return render(request, 'main/works.html')

def contacts(request):
    return render(request, 'main/contacts.html')

