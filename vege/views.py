from django.shortcuts import render,redirect
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

    return render(request,'recepies.html')