from django.urls import path
from . import views

from .views import ShortenerCreateApiView, ShortenerListAPIView

urlpatterns = [
    path('',views.index,name='Home'),
    path('login',views.handleLogin, name='Login'),
    path('signup',views.handleSignup, name='Signup'),
    path('dashboard', views.dashboard, name = 'Dashboard'),
    path('logout',views.handleLogout, name='Logout'),
    # api
    path('',ShortenerListAPIView.as_view(),name='all_links'),
    path('create/',ShortenerCreateApiView.as_view(),name='create_api'),
]
