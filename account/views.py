from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def account(request):
    context = {
        'test': 'test',
    }
    return render(request, 'account/account.html')

def login(request):
    context = {
        'test': 'test',
    }
    return render(request, 'account/login.html', context)