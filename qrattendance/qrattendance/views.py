from  datetime import datetime
from django.shortcuts import render, HttpResponse
def hello(request):
    
    return HttpResponse("Hello")
def hi(request):
    
    return HttpResponse("Hi")
def qr(request):
    
    return HttpResponse("showqr")
def hlw(request):
    
    return render(request,'new.html')