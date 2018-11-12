from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from .models import todoitem
def todoView(request):
    todoobjects=todoitem.objects.all()
    return render(request,'todo.html',{'todoitem':todoobjects})
# Create your views here.


def additem(request):
    # create todo item 
    # save the item to database
    # redirect to toditem
    # fint the name=contetn 
   
    new_item = todoitem(content = request.POST['addtext'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
def deleteitem(request, todo_id):
    # delete todo item
    itemdelete=todoitem.objects.get(id=todo_id)
    itemdelete.delete()
    
    return HttpResponseRedirect('/todo/')
