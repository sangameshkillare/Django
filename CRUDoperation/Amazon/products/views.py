from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
# Create your views here.


def product_list(request):
    products=Product.object.all()
    return render(request,'products/products_list.html',{'products':products})

 
def add_product(request):
    if request.method =='POST':
         Product.objects.create(
             name=request.POST['name'],
             price=request.POSt['price'],
             description=request.POST['description'],
             stock=request.POSt['stock'],
         )
        
         return redirect('products_list')
    return render(request,'products/add_products.html',{'products':Product})

def edit_prodect(request,id):
    Product=get_object_or_404(Product,id=id)
    if request.method =='POST':
       Product.name=request.POST['name']
       Product.price=request.POST['price'] 
       Product.description=request.POST['description']
       Product.stock=request.POST['stock']
       Product.save()
       return redirect('product_list')
    return render(request,'products/edit_product.html',{'product':Product})


def delete_product(request,id):
    product =get_object_or_404(Product,id=id)
    if request.method =='POST':
        product.delete()
        return redirect('products/product_list')
    
        