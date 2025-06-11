from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse # Placeholder
from .models import Warehouse, Product, Stock
# We will create forms later, for now, views will be simple.

def warehouse_list(request):
    # warehouses = Warehouse.objects.all()
    # return render(request, 'inventory/warehouse_list.html', {'warehouses': warehouses})
    return HttpResponse("Placeholder for warehouse list")

def warehouse_create(request):
    # if request.method == 'POST':
    #     # form = WarehouseForm(request.POST)
    #     # if form.is_valid():
    #     #     form.save()
    #     #     return redirect('inventory:warehouse_list')
    # else:
    #     # form = WarehouseForm()
    # # return render(request, 'inventory/warehouse_form.html', {'form': form})
    return HttpResponse("Placeholder for creating a new warehouse")

def warehouse_update(request, pk):
    # warehouse = get_object_or_404(Warehouse, pk=pk)
    # if request.method == 'POST':
    #     # form = WarehouseForm(request.POST, instance=warehouse)
    #     # if form.is_valid():
    #     #     form.save()
    #     #     return redirect('inventory:warehouse_list')
    # else:
    #     # form = WarehouseForm(instance=warehouse)
    # # return render(request, 'inventory/warehouse_form.html', {'form': form})
    return HttpResponse(f"Placeholder for updating warehouse {pk}")

def warehouse_delete(request, pk):
    # warehouse = get_object_or_404(Warehouse, pk=pk)
    # if request.method == 'POST':
    #     # warehouse.delete()
    #     # return redirect('inventory:warehouse_list')
    # # return render(request, 'inventory/warehouse_confirm_delete.html', {'warehouse': warehouse})
    return HttpResponse(f"Placeholder for deleting warehouse {pk}")


def product_list(request):
    # products = Product.objects.all()
    # return render(request, 'inventory/product_list.html', {'products': products})
    return HttpResponse("Placeholder for product list")

def product_create(request):
    # if request.method == 'POST':
    #     # form = ProductForm(request.POST)
    #     # if form.is_valid():
    #     #     form.save()
    #     #     return redirect('inventory:product_list')
    # else:
    #     # form = ProductForm()
    # # return render(request, 'inventory/product_form.html', {'form': form})
    return HttpResponse("Placeholder for creating a new product")

def product_update(request, pk):
    # product = get_object_or_404(Product, pk=pk)
    # if request.method == 'POST':
    #     # form = ProductForm(request.POST, instance=product)
    #     # if form.is_valid():
    #     #     form.save()
    #     #     return redirect('inventory:product_list')
    # else:
    #     # form = ProductForm(instance=product)
    # # return render(request, 'inventory/product_form.html', {'form': form})
    return HttpResponse(f"Placeholder for updating product {pk}")

def product_delete(request, pk):
    # product = get_object_or_404(Product, pk=pk)
    # if request.method == 'POST':
    #     # product.delete()
    #     # return redirect('inventory:product_list')
    # # return render(request, 'inventory/product_confirm_delete.html', {'product': product})
    return HttpResponse(f"Placeholder for deleting product {pk}")


def stock_levels_report(request):
    # stock_levels = Stock.objects.all().order_by('warehouse__name', 'product__name')
    # return render(request, 'inventory/stock_levels_report.html', {'stock_levels': stock_levels})
    return HttpResponse("Placeholder for stock levels report")
