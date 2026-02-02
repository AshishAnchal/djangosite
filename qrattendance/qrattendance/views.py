from  datetime import datetime
from django.shortcuts import render, HttpResponse
def hello(request):
    
    return HttpResponse("Hello")
def hi(request):
    
    return HttpResponse("Hi")
def qr(request):
    
    return HttpResponse("showqr")
def form(request):

    return render(request,'form.html')
def data(request):
    name=request.GET['uname']
    print(name)
    num=request.GET['unumber']
    print(num)
    rad=request.GET['iradio']
    print(rad)
    return render(request,"form.html")

def add(request):
    
    return render(request,'add.html')
def result(request):
    a=int(request.GET['enta'])
    b=int(request.GET['entb'])
    operate=request.GET['operate']
    result=""
    if operate=="ADD":
      result=a+b
    elif operate=="SUB":
         result=a-b
    print(a,b,operate,result)
    return render(request,'add.html')

