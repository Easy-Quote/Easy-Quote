from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    context = {
        'test': 'test'
    }
    return render(request, 'main/main.html', context)