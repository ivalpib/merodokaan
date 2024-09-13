from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from primary.form import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def HomeView(request):
    return render(request,'index.html')


def LoginView(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect('index')
       else:
            # Handle authentication failure
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    elif request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')

def RegistrationView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('login')
        
    else:
        form = UserRegistrationForm()
    
    return render(request,'registration.html', {'form':form})