from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import course, announcement, practice, CT, HW
from django.shortcuts import render, redirect

def home(request):
    all_course = course.objects.all()
    return render(request, 'elms/coursepage.html', {'all':all_course})

def search(request):
    return render(request, 'elms/search.html')

def individual(request):
    all_announcement = announcement.objects.all()
    all_practice = practice.objects.all()
    all_ct = CT.objects.all()
    all_hw = HW.objects.all()
    return render(request, 'elms/individuals.html', {'all':all_announcement,'prac' : all_practice, 'ct':all_ct, 'hw':all_hw})
    

def signin(request):
    if request.method == 'GET':
       return render(request, 'elms/index.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pass')
        user = authenticate(username = u, password = p)
        if user is None:
            return render(request, 'elms/index.html')
        else:
            login(request, user)
            return redirect('homepage')