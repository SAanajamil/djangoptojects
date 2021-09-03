from django.shortcuts import render, HttpResponse
from home.models import Registration

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        working_role = request.POST.get('working_role')
        analyst = request.POST.get('analyst')
        team = request.POST.get('team')
        manager = request.POST.get('manager')
        backup_person = request.POST.get('backup_person')
        job_nature = request.POST.get('job_nature')
        phone = request.POST.get('phone') 

        registration = Registration(name=name, email=email, password=password, working_role=working_role,
        analyst=analyst, team=team, manager=manager, backup_person=backup_person, job_nature=job_nature, phone=phone)

        registration.save()  

    return render(request, 'registration.html')




# Create your views here.
