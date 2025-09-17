from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def todo(request):
    tasks = Task.objects.all()
    return render(request, "todo.html", {"tasks": tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("todo")
    
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("todo")