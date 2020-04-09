from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def account(request):
    context = {
        'test': 'test',
    }
    return render(request, 'account/account.html', context)

@login_required(login_url='/account/login/')
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
    return redirect("../../")