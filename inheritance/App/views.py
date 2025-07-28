from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'App/home.html')  


def contact(request):
    return render(request,'App/contact.html')

def product(request):
    return render(request,'App/product.html')
