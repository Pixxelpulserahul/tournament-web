from django.shortcuts import render, redirect
from .forms import *
from .models import UserLogin



#================================================================================================
def home(request):
    form = LoginForm()
    return render(request, "index.html", {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            try:
                user = UserLogin.objects.get(username=username, password=password, email=email)
                return redirect("success")
            except UserLogin.DoesNotExist:
                return render(request, "UserNotFound.html")

                
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

#================================================================================================

def success_view(request):
    return render(request, "success.html")

#================================================================================================

def signup_home(request):
    form = LoginForm()
    return render(request, "SignUp.html", {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                user = UserLogin.objects.get(email=email)
                return render(request, "alreadyExist.html")
            except:
                user = UserLogin(username=username, password=password, email=email)
                user.save()
                return redirect("success")
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

#================================================================================================
