from  datetime import datetime
from django.shortcuts import render, HttpResponse,redirect
def hello(request):
    
    return render(request,"images.html",{"greeting":"Good Morning","image":"Ashish.jpg"})
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
    if request.GET:
        
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

def form1(request):
    a=0
    b=0
    result=""
    if request.POST:
        a=int(request.POST['a'])
        b=int(request.POST['b'])
        cmd=request.POST['cmd']
        # print(cmd)
        if cmd=="Add":
            result=a+b
        elif cmd=="Sub":
            result=a-b
    return render (request,'form1.html',{"a":a,"b":b,"result":result}) 


def check(request):

    result = {
        100: "Pass",101: "Fail",102: "Pass", 103: "Fail",}
    roll=""
    
    if request.POST:
        roll=int(request.POST['r'])
        result=result.get(roll,"Not found")
        print(roll)    
        
    return render(request, "class.html", {"roll": roll,"result":result})

def veg(request):

    vegetables = {
        "Potato":"20kg","Brinjal":"15kg"}
    cod=""
    
    if request.POST:
        cod=(request.POST['a'])
        print(cod)
        vegetables=vegetables.get(cod,"Not found")
    
        
    return render(request, "veg.html", {"cod": cod,"vegetables":vegetables})

def sessionadd(request):
    a=0
    if request.POST:
        
     a=request.POST['enta']
     b=request.POST['entb']
     session=request.session
     session["name"]=a
     print(session["name"],b)
    return render(request,"form2.html")
def sessionremove(request):
    session=request.session
    session.pop("name")
    return HttpResponse("Session Remove")

def sessionview(request):
    session=request.session
    name=request.session["name"]
    if name is None:
        name="None"
    return HttpResponse("Session View "+name)

def dologin(request):
    result=""
    username=""
    pwd=""
    uname={"Ashish":"1234","Aryan":"1234"}
    if request.POST:
        username=request.POST['enta']
        pwd=request.POST['entb']
        result=uname.get(username,None)
        if result is None:
            return render(request,"login.html",{"result":"Invalid","username":username,"pwd":pwd})
        if pwd==result:
              session=request.session
              session['username']=username
              redirect("/protected")
              return render(request,"show.html",{"username":username,"image":username + ".jpg"})

        return render(request,"login.html",{"result":"Invalid","username":username,"pwd":pwd})
    return render(request,"login.html",{"result":"","username":"","pwd":""})
        
def protected(request):
    session=request.session
    username=request.session.get("username")
    if username is None:
        username=""
        return redirect("/dologin",{"username":username,"image":username + ".jpg"})       
    # return render(request,"show.html")
def dologout(request):
    session=request.session
    session.pop("username")
    return redirect("/dologin")