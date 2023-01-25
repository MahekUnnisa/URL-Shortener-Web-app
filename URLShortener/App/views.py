from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'App/index.html')

def handleLogin(request):
    # return render(request,'App/login.html')

    if request.method == "POST":
        loginemail = request.POST.get('loginemail', False)
        loginpassword = request.POST.get('loginpassword', False)

        user = authenticate(username = loginemail, password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect('/')
        else:
            messages.success(request, 'Invalid Credentials, please try again')
            return redirect('/')
    return HttpResponse('404 - Not Found')

def handleSignup(request):
    if request.method=='POST':
        
        full_name = request.POST.get('full_name', False)
        phone_number = request.POST.get('phone_number', False)
        occupation = request.POST.get('occupation', False)
        email  = request.POST.get('email',False)
        password  = request.POST.get('password',False)
        confirmpassword  = request.POST.get('confirmpassword',False)
        # Create the user
        # get the post parameter
        if len(full_name) > 20:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        if len(phone_number) >12:
            messages.error(request, 'Phone number should be under 12 characters')
        if password != confirmpassword:
            messages.error(request,"Passwords do not match")
            return redirect('/')
        if not full_name.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect('/')
        myuser = User.objects.create_user(full_name=full_name,email=email,password=password, phone=phone_number, occupation=occupation)
        myuser.save()
        messages.success(request, "You are registered successfully") 
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

    # return render(request,'App/signup.html')

def dashboard(request):
    if  not request.user.is_authenticated:
        messages.error(request, 'Login reguired')
        return render(request,'App/login.html')
    else:
        return render(request,'App/dashboard.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')