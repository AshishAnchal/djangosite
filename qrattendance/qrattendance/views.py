from  datetime import datetime
from django.shortcuts import render, HttpResponse
def hello(request):
    
    return render(request,"images.html",{"greeting":"Good Morning"})
def result(request):
    a=0
    b=0
    if request.GET:
        a=int(request.GET['enta'])
        b=int(request.GET['entb'])
        cmd=request.GET['result']
        result=""
        if cmd=="add":
            result=a+b
        elif cmd=="sub":
            result=a-b
        elif cmd=="Mux":
            result=a*b   
        elif cmd=="Div":
            result=a/b     
        print(a,b,cmd)
    return render(request,'hello.html',{"a":a,"b":b,"result":(result)})

def radio(request):
    a=0
    b=0
    result=""
    if request.GET:
        a=int(request.GET['enta'])
        b=int(request.GET['entb'])
        cmd=request.GET['op']
        
        if cmd=="add":
            result=a+b
        elif cmd=="sub":
            result=a-b   
        elif cmd=="Mux":
            result=a*b   
        elif cmd=="Div":
            result=a/b        
        print(a,b,cmd)
    return render(request,'radio.html',{"a":a,"b":b,"result":(result)})
from django.shortcuts import render

def open(request):
    
    
    return render(request, 'form.html')

def data(request):
    print("data")
    name = request.GET['name']
    pas = request.GET['pass']
    add = request.GET['Add']
    brand = request.GET['iradio']
    a = request.GET['on']
    r = request.GET['off']
    
    prot = request.GET['drop']

    print(name, pas, add,a,r, brand, prot)
    return render(request,'form.html')


def chek(request):
    return render (request,'check.html')

def now(request):
 a=request.GET['p']
 b=request.GET['n']
 print(a,b)
 return render (request,'check.html')

def merge(request):
    a=0
    b=0
    result=""
    if request.GET:
        a=int(request.GET['a'])
        b=int(request.GET['b'])
        cmd=request.GET['cmd']
        if cmd=="Add":
            result=a+b
        elif cmd=="Sub":
            result=a-b
    return render (request,'merge.html',{"a":a,"b":b,"result":result})        