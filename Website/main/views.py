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

def contact_me(request):
    context = {}
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
        context['form'] = form
        return render (
            request,
            'contacts.html',
            context=context
        )
