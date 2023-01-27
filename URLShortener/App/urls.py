from django.urls import path
from . import views
from .views import ShortenerCreateApiView, ShortenerListAPIView

urlpatterns = [
    path('',views.index,name='Home'),
    # Auth
    path('signup',views.handleSignup, name='Signup'),
    path('login',views.handleLogin, name='Login'),
    path('logout',views.handleLogout, name='Logout'),
    
    path('dashboard', views.dashboard, name = 'Dashboard'),
    path('create',views.create, name='Create New Link'),
    path('linkdetails/<int:link_id>/', views.linkDetails, name='Link Details'),
    # api
    path('',ShortenerListAPIView.as_view(),name='all_links'),
    path('api/create/',ShortenerCreateApiView.as_view(),name='create_api'),
]
