from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404

from rest_framework.generics import ListAPIView,CreateAPIView
from django.views import View
from django.conf import settings

from .models import Link
from .serializers import LinkSerializer

import re
import datetime
import pytz
# to check if name has only letters and space
def is_valid_name(name):
    pattern = r'^[a-zA-Z\s]+$'
    return bool(re.match(pattern, name))

# Create your views here.
def index(request):
    return render(request,'App/index.html')

def handleLogin(request):
    # return render(request,'App/login.html')
    if request.method == "POST":
        loginemail = request.POST.get('loginemail', False)
        loginname = request.POST.get('loginname', False)
        loginpassword = request.POST.get('loginpassword', False)

        user = authenticate(username = loginname,email=loginemail, password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully logged in")
            return redirect('/dashboard')
        else:
            messages.success(request, 'Invalid Credentials, please try again')
            return redirect('/login')
    return render(request,'App/login.html')

def handleSignup(request):
    if request.method=='POST':
        
        full_name = request.POST.get('full_name', False)
        email  = request.POST.get('email',False)
        password  = request.POST.get('password',False)
        confirmpassword  = request.POST.get('confirmpassword',False)
        # Create the user
        # get the post parameter
        if len(full_name) > 20:
            messages.error(request, "Name must be under 20 characters")
            return redirect('/signup')
        if password != confirmpassword:
            messages.error(request,"Passwords do not match")
            return redirect('/signup')
        if not is_valid_name(full_name):
            messages.error(request,"Name should only contain letters")
            return redirect('/signup')
        myuser = User.objects.create_user(username=full_name,email=email,password=password)
        myuser.save()
        messages.success(request, "You are registered successfully") 
        return redirect('/login')
    else:
        return render(request,'App/signup.html')

    # return render(request,'App/signup.html')

def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Login reguired')
        return render(request,'App/login.html')
    else:
        return render(request,'App/dashboard.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

# Api views
class ShortenerListAPIView(ListAPIView):
    queryset=Link.objects.all()
    serializer_class=LinkSerializer

class ShortenerCreateApiView(CreateAPIView):
    serializer_class=LinkSerializer


class Redirector(View):
    def get(self,request,custom_string,random_string,*args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+custom_string+'/'+random_string
        link = get_object_or_404(Link,shortened_link = shortener_link)
        if link.is_expired:
            raise Http404("This link has expired.")
        link.click_count +=1
        link.save()
        return redirect(link.original_link)


