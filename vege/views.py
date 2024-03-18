from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpRequest
from .models import *

def receipes(request):
    
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('pic')
        name=data.get('name')
        desc=data.get("desc")
        
        print(name)
        print(desc)
        print(image)
        
        vege_data.objects.create(
                name=name,
                pic=image,
                desc=desc,
        )  
        
        return redirect('/receipes')
    queryset=vege_data.objects.all()
    context=({'vege_data':queryset})

    return render(request,'recepies.html',context)


def delete_receipes(request, id):
    queryset=vege_data.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')


def update_receipes(request,id):
    queryset = vege_data.objects.get(id = id)
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('pic')
        name=data.get('name')
        desc=data.get("desc")
    
    
        queryset.name=name
        queryset.desc=desc
        
        if image:
            queryset.pic=image
        else:
            pass
        
        queryset.save()
    
    context={'receipe_update':queryset}
    return render(request,'update.html',context)