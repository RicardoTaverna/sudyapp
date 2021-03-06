from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile')
]