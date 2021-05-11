from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def index(request):
    if request.method=="POST":
        contact=Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        
        contact.name=name
        contact.email=email
        contact.subject=subject
        
        contact.save()
        
        return render(request, 'master.html')
    
    return render(request, 'index.html')
