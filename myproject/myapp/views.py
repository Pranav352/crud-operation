from django.shortcuts import render,HttpResponse,redirect
from .models import*
# Create your views here.

def crud(request):
    if request.POST:
        name=request.POST["name"]
        email=request.POST["email"]
        address=request.POST["address"]
        phone=request.POST["phone"]

        Employee.objects.create(name=name,email=email,address=address,phone=phone)

    return redirect("read")

def read(request):
    uid=Employee.objects.all()
    
    context={"uid":uid}
    return render(request,"crud.html",context)



def update(request,id):
    uid=Employee.objects.get(id=id)
    if request.POST:
        name=request.POST["name"]
        email=request.POST["email"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        
        uid.name=name
        uid.email=email
        uid.address=address
        uid.phone=phone
        uid.save()
    return redirect("read")

def delete_data(request,id):
    uid=Employee.objects.get(id=id)
    uid.delete()
    return redirect("read")