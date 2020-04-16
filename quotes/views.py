from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import Quote101
from .models import Quote202

# Create your views here.

def quotes(request):
    context = {
        'test': 'test',
    }
    return render(request, 'quotes/quotes.html', context)

def edit_quote(request):
    return HttpResponse('edit an old quote here')

def get_form(request):
    form = Quote101(request.POST or None)
    if form.is_valid():
        form.save()
        form = Quote101()
    user = request.user
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'quotes/new_quote.html', context)
