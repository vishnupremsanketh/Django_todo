from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from .models import products 
def todoView(request):
    todoobjects=products.objects.all()
    
    return render(request,'todo.html',{'todoitem':todoobjects})
# Create your views here.


def additem(request):
    # create todo item 
    # save the item to database
    # redirect to toditem
    # fint the name=contetn 
   
    add_name = products(name = 'name' in request.POST and request.POST['name'],
                        address = 'address' in request.POST and request.POST['address'],
                        phoneNumber = 'phonenumber' in request.POST and request.POST['phonenumber'],
                        pinCode = 'pincode' in request.POST and request.POST['pincode'])
    
    #products.save()
    add_name.save()
    
    return HttpResponseRedirect('/todo/')
    db.connections.close_all()
def deleteitem(request, todo_id):
    # delete todo item
    itemdelete=products.objects.get(id=todo_id)
    itemdelete.delete()
    
    return HttpResponseRedirect('/todo/')
