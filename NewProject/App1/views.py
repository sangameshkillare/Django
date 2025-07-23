from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#context dictionary of contec variable .

def hello(request):
    return render(request,'App1/hello.html',{'name':'Sangamesh'})
