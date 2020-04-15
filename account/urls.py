from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import user_passes_test


App_name = 'account'
urlpatterns = [
    path('', views.account, name='account'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
