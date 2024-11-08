from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from . import models


# Create your views here.
def home(request):
    return render(request, 'base.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if user.check_password(password):
                return redirect("home")
            else:
                return JsonResponse({"error": "wrong password"})
        else:
            return JsonResponse({"error": "user does not exist"})
        
    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        username = request.POST["username"]
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "this username is already exists"})
        elif User.objects.filter(email=email).exists():
            return JsonResponse({"error": "this email is already exists"})
        else:  
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            if user != None:
                return redirect("login")
    return render(request, 'register.html')

def hotels(request):
    return render(request, 'hotels.html')

def flights(request):
    return render(request, 'flights.html')

def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return render(request, 'logout.html')