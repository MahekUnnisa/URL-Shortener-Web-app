from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from django.contrib.auth.models import User
from .models import Link

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

from rest_framework.generics import ListAPIView,CreateAPIView
from django.views import View

from .forms import LinkForm
from .serializers import LinkSerializer

import re
import datetime

#  Web views

# Home page
def index(request):
    return render(request,'App/index.html')

def handleLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in")
                return redirect('/dashboard')

            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm(data=request.POST)

    return render(request, 'App/registrations/login.html', {'form': form})

# View uses inbuilt django user model named "User"
def handleSignup(request):
    if request.method=='POST':
        
        full_name = request.POST.get('full_name', False)
        email  = request.POST.get('email',False)

        password  = request.POST.get('password',False)
        confirmpassword  = request.POST.get('confirmpassword',False)

        # Validations
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
        return render(request,'App/registrations/signup.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

# All links page
def dashboard(request):
    # Links from only logged in user
    links = Link.objects.filter(user=request.user)
    # Orders from latest to old
    links = Link.objects.all().order_by('-created_at')

    context = {'links': links}
    return render(request,'App/dashboard.html', context)

# Create a new link
def create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save()
            link.shortener()
            link.save()
            return redirect('App:linkDetails', link_id=link.id)
    else:
        form = LinkForm(request.GET)
    return render(request, 'App/create.html', {'form' : form })

# Each link details after creating it
def linkDetails(request,link_id):
    link = Link.objects.get(id=link_id)

    context = {'shortened_link': link.shortened_link, 'expiration_date': link.expiration_date, 'click_count':link.click_count, 'original_link':link.original_link, 'created_at':link.created_at}

    return render(request, 'App/linkDetails.html', context)

# Api views
class ShortenerListAPIView(ListAPIView):
    queryset=Link.objects.all()
    serializer_class=LinkSerializer

class ShortenerCreateApiView(CreateAPIView):
    serializer_class=LinkSerializer

# Redirects user to the created link on click
class Redirector(View):
    def get(self,request,custom_string,random_string,*args, **kwargs):

        shortener_link=settings.HOST_URL+'/'+custom_string+'/'+random_string
        link = get_object_or_404(Link,shortened_link = shortener_link)

        if link.expiration_date.replace(tzinfo=None) < datetime.datetime.now():
            raise Http404("This link has expired.")

        link.click_count +=1
        link.save()

        redirect_link=Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)

# Utility

# To check if name has only letters and space in auth forms
def is_valid_name(name):
    pattern = r'^[a-zA-Z\s]+$'
    return bool(re.match(pattern, name))