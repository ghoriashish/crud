from django.shortcuts import render,HttpResponseRedirect,reverse
from . models import *
# Create your views here.
def homepage(request):
    return render(request,"app/home.html")
def success(request):
    return render(request,"app/data.html")


def registeruser(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    newuser=user.objects.create(fname=fname,lname=lname)
    return HttpResponseRedirect(reverse('showdata'))

def showdata(request):
    alluser=user.objects.all()
    return render(request,"app/data.html",{'key':alluser})
def edit(request):
    e=request.POST['e']
    new=user.objects.filter(id=e)
    return render(request,"app/edit.html",{'key1':new})    
def change(request):
    u=request.POST['fname']
    v=request.POST['lname']
    ide=request.POST['i']
    newuser=user.objects.get(id=ide)

    if u=="":
        pass
    else:
        newuser.fname=u
        newuser.save()
    
    if v=="":
        pass
    else:
        newuser.lname=v
        newuser.save()    
    alluser=user.objects.all()
    return render(request,"app/data.html",{'key':alluser})
def delete(request):
    d=request.POST['d']
    oneuser=user.objects.filter(id=d)
    oneuser.delete()
    alluser=user.objects.all()
    return render(request,"app/data.html",{'key':alluser})