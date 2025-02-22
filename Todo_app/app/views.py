from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        list_item(title=title,
                  description=description).save()
        return redirect('create')
    data = list_item.objects.all()
    return render(request,'home.html',{'data': data})

def edit(request,id):
    dataget = list_item.objects.get(id = id)
    data = list_item.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        dataget.title = title
        dataget.description = description
        dataget.save()
        return redirect('create')
    return render(request,'home.html',{'dataget':dataget,'data':data})

def delete(request,id):
    dataget = list_item.objects.get(id=id)
    dataget.delete()
    return redirect('create')

