from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from rest_framework.generics import ListAPIView,CreateAPIView
from django.views import View
from django.conf import settings

from .models import Link
from .serializers import LinkSerializer

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
    return render(request,'App/login.html')

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
    def get(self,request,shortener_link,*args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link=Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)