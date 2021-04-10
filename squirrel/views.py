from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel/index.html',context)

def create_squirrel(request):
    if request.method=='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/squirrel/')
    else:
        form = SquirrelForm(request.POST)
        contect={
                'form'=form,
                }
    return render(request,'sightings/create.html',context)

def update_squirrel(request,Unique_Squirrel_ID):
    squirrel= Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/squirrel/')
    else:
        form = SquirrelForm(instance=squirrel)
    context ={
            'form':form,
             }
    return render(request, 'sightings/update.html', context)









# Create your views here.
