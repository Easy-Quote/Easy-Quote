from django.urls import path

from . import views

App_name = 'items'
urlpatterns = [
    path('', views.items, name='items'),
    path('edit/', views.edit_items, name='edit_items'),
    path('importcsv/', views.importcsv, name='import_csv'),
]
