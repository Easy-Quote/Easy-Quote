from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

App_name = 'account'
urlpatterns = [
    path('', views.account, name='account'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
]
