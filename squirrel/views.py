from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Squirrel

def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel/sightings.html',context)

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
    return render(request,'squirrel/create.html',context)

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
    return render(request, 'squirrel/update.html', context)

def stats(request):












# Create your views here.
