from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all() #models에서 등록한 함수 이름이 Task

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def update_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'update_task.html', context)

def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'delete.html', context)