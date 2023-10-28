from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from new_app.forms import TodoForm
from new_app.models import Todo


# Create your views here.
def new(request):
    return render(request, template_name="index.html")


def index_admin(request):
    return render(request, template_name="index_admin.html")


# create
def create(request):
    form = TodoForm()
    if request.method == "POST":
        form1 = TodoForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('readuser')
        else:
            form = form1
    else:
        initial_data={'date': timezone.now().date()}
        form = TodoForm(initial=initial_data)
    return render(request, "add.html", {"form": form})


def readuser(request):
    data1 = Todo.objects.all()
    return render(request, "index_admin.html", {"data": data1})


# delete-data
def delete(request, id):
    if request.method == 'POST':
        delt = Todo.objects.get(id=id)
        delt.delete()
        return redirect("readuser")
    return render(request, "index_admin.html")


# update_data
def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form1 = TodoForm(request.POST, instance=todo)
        if form1.is_valid():
            form1.save()
            return redirect("readuser")
        # else:
        #     messages.info(request,"Due invalid")
    return render(request, "update.html", {'form': form})
