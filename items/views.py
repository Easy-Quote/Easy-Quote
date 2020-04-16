from django.shortcuts import render, redirect
from django.http import HttpResponse
from items.models import inventory
from items.forms import Inventory1
from django.contrib.auth.decorators import permission_required


# Create your views here.

def items(request):
    columns = ['Code', 'Description', 'Price']
    context = {
        'test': inventory.objects.all(),
        'column_list': columns,
        'inventory': inventory,
    }
    return render(request, 'items/items.html', context)

@permission_required('items.change_inventory', login_url='/account/login/')
def edit_items(request):
    if request.method == 'POST':
        print(request.POST.get('items'))
        print(request.POST.get('item_code'))
        if 'edit_item' in request.POST:
            item_id = request.POST.get('items')
            item1 = inventory.objects.get(pk=item_id)
            print(item1)
            form = Inventory1(instance=item1)
            context = {
                'form': form,
                'code': item_id,
            }
            return render(request, 'items/editor.html', context)
        elif 'delete_item' in request.POST:
            model = inventory(pk=request.POST.get('items'))
            model.delete()
            return redirect('/items')
        elif "edited" in request.POST:
            item_code = request.POST.get('item_code')
            item = inventory.objects.get(pk=item_code)
            form = Inventory1(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('/items')
            else:
                form = Inventory1(instance=item)
                context = {
                    'form': form,
                }
                return render(request, 'items/editor.html', context)
        else:
            return HttpResponse('Something went wrong')
    else:
        columns = ['Code', 'Description', 'Price']
        RequestContext = {
            'test': inventory.objects.all(),
            'column_list': columns,
            'inventory': inventory,
        }
        return render(request, 'items/edit.html', RequestContext)

def importcsv(request):
    data = {}
    if request.method == 'POST':
        csvfile = request.FILES['myfile']
        if csvfile != None:
            print(csvfile)
            lines = csvfile.read().split(b'\r\n')
            print(csvfile.read().decode("utf-8"))
            print(lines)
            del lines[0]
            del lines[-1]
            for line in lines:
                print(line)
                fields = line.decode("utf-8").split(";")
                data_dict = {}
                data_dict["item_code"] = fields[0]
                data_dict["item_description"] = fields[1]
                data_dict["item_price"] = fields[2]
                form = Inventory1(data_dict)
                print(form)
                if form.is_valid():
                    print(form.is_valid())
                    form.save()
                else:
                    print(form.is_valid())
                    pass
            return redirect('/items')

def new_item(request):
    if request.method == 'POST':
        form = Inventory1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/items')
    elif request.method == 'GET':
        form = Inventory1()
        context = {
            'form': form,
        }
        return render(request, 'items/new.html', context)