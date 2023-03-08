from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Task, Priority
from django.contrib.auth.models import User
from .forms import AddTaskForm, UpdateTaskForm
from django.contrib import messages



# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = request.user
        tasks = user.user_tasks.all()
        add_task_form = AddTaskForm()
        return render(request, "home/dashboard.html", {
            "tasks" : tasks,
            "form" : add_task_form,
            
        })    
    return redirect("login_user")



def remove_task(request, task_id):
    
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()     
        messages.warning(request,"Task Successfully Deleted")
        return HttpResponseRedirect(reverse("home"))
    
    except:
        return HttpResponse("error")

    

def add_task(request):
    if request.method == "POST":
        task_user = request.user
        form = AddTaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Task.objects.create(
                task_name = cd['task_name'],
                task_description = cd['task_description'],
                task_priority = cd['task_priority'],
                task_user = request.user
            )
            messages.success(request, "Task Added Successfully")
            return redirect('home')
        messages.error(request, "Not valid input", "danger-coustom")
        return redirect('home') 
    
    return redirect('home')


def change_priority(request, task_id):
    task = Task.objects.get(pk=task_id)
    if not task.task_status :
        task.task_status = True
        task.save()
    else:
        task.task_status = False
        task.save()
    return HttpResponseRedirect(reverse("home"))



        
        

def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Successfully")
            return redirect("home")

    update_form = UpdateTaskForm(instance=task)
    return render(request, "home/updateForm.html", {
        "updateForm":update_form,
        "task" : task
    })