from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def account(request):
    return HttpResponse( request ,"account home page")

def  login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the user exists
        if not User.objects.filter(username=email).exists():
            messages.error(request, 'User does not exist')
            return redirect('login')
        
        # Check if the user is active
        user = User.objects.get(username=email)
        if not user.is_active:
            messages.error(request, 'User is inactive')
            return redirect('login')
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'auth/login.html')  
  
def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        full_name = full_name.split(' ')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
              
        # Create a new user
        user = User.objects.create_user(username=email, password=password, email=email, first_name=full_name[0], last_name=full_name[1] if len(full_name) > 1 else '')
        user.save()
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong')
            return redirect('register')
    return render(request, 'auth/register.html')    

def logout_page(request):
    logout(request)
    return redirect('home')