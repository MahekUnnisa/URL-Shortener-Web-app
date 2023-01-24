from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'App/index.html')

def login(request):
    return render(request,'App/login.html')

def signup(request):
    return render(request,'App/signup.html')

def dashboard(request):
    return render(request,'App/dashboard.html')