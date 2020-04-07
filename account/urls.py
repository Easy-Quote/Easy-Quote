from django.urls import path

from . import views

App_name = 'account'
urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.login, name='login'),
]