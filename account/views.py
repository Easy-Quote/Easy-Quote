from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.

def account(request):
    context = {
        'test': 'test',
    }
    return render(request, 'account/account.html', context)

def profile(request):
    if request.user != None:
        user1 = request.user
        print(user1)
    else:
        user1 = None
    context = {
        'user': user1,
    }
    return render(request, 'account/profile.html', context)

def logout_view(request):
    logout(request)