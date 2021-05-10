from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.contrib.contenttypes.models import ContentType

# Views created here

def task_new(request):
    if not request.user.is_authenticated:
        raise Http404("LOGIN REQUIRED!")
    form = TaskForm(request.POST or None, request.FILES or None)
    if form.is_Valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "New task added successfully")
        return redirect("TimeEntSys:new")

    context = {
                "form": form,
                "title": "New Task"
              }
    return render(request, "task_new.html", context)

def task_all(request):
    if not request.user.is_authenticated:
        raise Http404("LOGIN REQUIRED!!!")
    tasks = Task.objects.all()
    tasks = tasks.filter(publish__lte=timezone.now())
    tasks = tasks.order_by("timestamp")

    search_q = request.GET.get("search")
    if search_q:
        tasks = tasks.filter(title__icontains=search_q)

    j_paginator = Paginator(tasks, 3)
    page = request.GET.get("page")
    tasks = j_paginator.get_page(page)


    context = {
                "title": "All Tasks",
                "tasks": tasks
              }
    return render(request, "tasks_all.html", context)

def taskDetails(request, inp_id):
    instance = get_object_or_404(Task, id=inp_id)
    context = {
                "title": instance.id,
                "task": instance
              }
    return render(request, "task_details.html", context)

def task_edit(request, inp_id):
    if not request.user.is_authenticated:
        raise Http404("LOGIN REQUIRED!!!")
    task = get_object_or_404(Task, id=inp_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Task edited successfully")
        return redirect("TimeEntSys:ByID", inp_id=instance.id)

    context = {
                "title": "Edit",
                "form": form
              }
    return render(request, "task_edit.html", context)

def task_delete(request, inp_id):
    if not request.user.is_authenticated:
        raise Http404("LOGIN REQUIRED!!!")
    task = get_object_or_404(Task, id=inp_id)
    print(task)
    print(request.POST)
    if "yes" in request.POST:
        task.delete()
        return redirect("TimeEntSys:all")
    elif "no" in request.POST:
        return redirect("TimeEntSys:ByID", inp_id=task.id)
    
    context = {
                "title": "Delete",
                "task": task
              }

    return render(request, "task_delete.html", context)