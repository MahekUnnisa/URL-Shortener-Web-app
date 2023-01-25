from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('login',views.handleLogin, name='Login'),
    path('signup',views.handleSignup, name='Signup'),
    path('dashboard', views.dashboard, name = 'Dashboard'),
    path('logout',views.handleLogout, name='Logout')
]