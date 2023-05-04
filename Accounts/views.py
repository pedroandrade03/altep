from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import Http404

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.POST:
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        remember = request.POST.get('remember', False)
        
        usernameExists  = User.objects.filter(username=username).exists()
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if username:
            if user is not None:
                auth.login(request, user)
                user = True
                if not remember:
                    request.session.set_expiry(0)
        return JsonResponse({'username': usernameExists , 'password': user,'remember':remember})
    return render(request, 'accounts/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'accounts/register.html')

def forgot(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'accounts/forgot.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
