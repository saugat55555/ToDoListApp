from django.shortcuts import render, redirect
from .models import Lists
from .forms import Form
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == "POST":
        form = Form(request.POST or None)
        if form.is_valid():
            form.save()
            hello = Lists.objects.all()
            messages.success(request, "Congratulation, you've added an item successfully!")
            return render(request, 'base.html', {'hello':hello})

    else:
        hello = Lists.objects.all()
        return render(request, 'base.html', {'hello':hello})


def delete(request, list_id):
    items = Lists.objects.get(pk = list_id)
    items.delete()
    messages.success(request, "Your task has been deleted")
    return redirect('index')

def cross(request, list_id):
    items = Lists.objects.get(pk = list_id)
    items.done = True
    items.save()
    return redirect('index')

def uncross(request, list_id):
    item = Lists.objects.get(pk = list_id)
    item.done = False
    item.save()
    return redirect('index')