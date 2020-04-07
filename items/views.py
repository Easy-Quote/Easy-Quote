from django.shortcuts import render
from django.http import HttpResponse
from items.models import inventory

# Create your views here.

def items(request):
    columns = ['Code', 'Description', 'Price']
    context = {
        'test': inventory.objects.all(),
        'column_list': columns,
        'inventory': inventory,
    }
    return render(request, 'items/items.html', context)

def edit_items(request):
    columns = ['Code', 'Description', 'Price']
    RequestContext = {
        'test': inventory.objects.all(),
        'column_list': columns,
        'inventory': inventory,
    }
    return render(request, 'items/edit.html', RequestContext)
