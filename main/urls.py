from django.urls import path

from . import views

App_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
]