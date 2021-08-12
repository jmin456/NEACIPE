from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, "home.html")

def search(request):
    return render(request, "search.html")

# def result(request):
#     checks=request.POST.getlist('checks[]')
#     return render(request, "result.html",{'checks':checks})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def signup(request):
    if request.method == 'POST':
        try:
            if request.POST['password'] == request.POST['confirm']:
                user = User.objects.create_user(
                                                username=request.POST['username'],
                                                password=request.POST['password'],
                                               )
                auth.login(request, user)
                return redirect('home')
            return render(request, 'signup.html')
        except:
            return render(request, 'signup.html')
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        try:
            if request.POST['password'] == request.POST['confirm']:
                user = User.objects.create_user(
                                                username=request.POST['username'],
                                                password=request.POST['password'],
                                               )
                auth.login(request, user)
                return redirect('home')
            return render(request, 'signupagain.html')
        except:
            return render(request, 'signupagain.html')
    return render(request, 'signup.html')

def signupagain(request):
    if request.method == 'POST':
        try:
            if request.POST['password'] == request.POST['confirm']:
                user = User.objects.create_user(
                                                username=request.POST['username'],
                                                password=request.POST['password'],
                                               )
                auth.login(request, user)
                return redirect('home')
            return render(request, 'signupagain.html')
        except:
            return render(request, 'signupagain.html')
    return render(request, 'signupagain.html')
