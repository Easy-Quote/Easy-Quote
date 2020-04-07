from django.urls import path

from . import views

App_name = 'quotes'
urlpatterns = [
    path('', views.quotes, name='quotes'),
    path('new/', views.get_form, name='new_quote'),
    path('edit/', views.edit_quote, name='edit_quote'),
]