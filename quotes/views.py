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

# def new_quote(request):
#     context = {
#         'test': 'test',
#     }
#     return render(request, 'quotes/new_quote.html', context)

def edit_quote(request):
    return HttpResponse('edit an old quote here')

# def get_form(request):
#     if request.method == 'POST':
#         form = Quote101(request.POST)
#         if form.is_valid():
#             Quote202.objects.create(**form.cleaned_data)
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = Quote101()

#     return render(request, 'quotes/new_quote.html', {'form': form})

def get_form(request):
    form = Quote101(request.POST or None)
    if form.is_valid():
        form.save()
        form = Quote101()
    
    context = {
        'form': form,
    }
    return render(request, 'quotes/new_quote.html', context)
 