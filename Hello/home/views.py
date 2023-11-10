from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def home(request):
    messages.success(request,"this is a test msg")
    return render(request,'index.html')

def router(request):
    return render(request,'routers.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Message has been sent")

    return render(request,'contact.html')
