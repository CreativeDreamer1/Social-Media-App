from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, LogInForm

# This code leads user to signup and login page 

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("users:login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {
        'signupform': form
    })

# This view verifies if the data entered is correct and logs user in

def login(request):
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("posts:index")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LogInForm()
    return render(request, 'users/login.html', {
        'loginform': form,
    })