from django.shortcuts import render, redirect
from .models import Task   
from .forms import *        # this is imported to display our fields to the user 
                            #which are in database


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks:list')     # or use redirect('/') to remain in same homepage

    context = {'tasks':tasks, 'form':form} #values to be display to the user with the help of template
    return render(request,'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form  = TaskForm(instance=task)
    if request.method == 'POST':
        form  = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks:list')

    context = {'form':form}
    return render(request, 'tasks/update_task.html',context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('tasks:list')
    
    context = {'item':item}
    return render(request,'tasks/delete.html',context)