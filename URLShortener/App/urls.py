from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ShortenerCreateApiView, ShortenerListAPIView

urlpatterns = [
    path('',views.index,name='Home'),
    path('login/',views.handleLogin, name='login'),
    path('signup',views.handleSignup, name='Signup'),
    path('dashboard', views.dashboard, name = 'Dashboard'),
    path('logout',views.handleLogout, name='Logout'),
    path('create/',views.create, name='CreateNewLink'),
    # api
    path('',ShortenerListAPIView.as_view(),name='all_links'),
    path('api/create/',ShortenerCreateApiView.as_view(),name='create_api'),
]
