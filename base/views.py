from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/form')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('/login')

    return render(request, 'login.html')


def registerPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            return redirect('/register')

        user = User.objects.create_user(
            first_name=name,
            username=username,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('/login')
    
    return render(request, 'register.html')

@login_required(login_url="/login")
def formPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone_no = request.POST.get('phone_no')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        hobbies = request.POST.getlist('hobbies')
        country = request.POST.get('country')
        bio = request.POST.get('bio')
        form = UserForm(name=name, age=age, phone_no=phone_no, date_of_birth=date, gender=gender, hobbies=', '.join(hobbies), country=country, bio=bio)
        form.save()
        messages.success(request, "Form submitted successfully!")
        return redirect('/form')
    return render(request, 'info_form.html')

def viewForms(request):
    forms = UserForm.objects.all()
    return render(request, 'all_forms.html', {'forms': forms})

def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/login')