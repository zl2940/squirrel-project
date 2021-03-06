from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min, Count, Q
from .models import Squirrel
from .forms import SquirrelForm

def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel/sightings.html',context)

def add(request):
    if request.method=='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/squirrel/sightings.html')
    else:
        form = SquirrelForm(request.POST)
    context={
            'form':form,
            }
    return render(request,'squirrel/add.html',context)

def update(request,Unique_Squirrel_ID):
    squirrel= Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect('/squirrel/sightings.html')
    else:
        form = SquirrelForm(instance=squirrel)
    context={
            'form':form,
            }
    return render(request, 'squirrel/add.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()
    Total=len(squirrels)
    Adult_count=Squirrel.objects.filter(Age="Adult").count()
    Juvenile_count=Squirrel.objects.filter(Age="Juvenile").count()
    Gray_count=Squirrel.objects.filter(Primary_Fur_Color="Gray").count()
    Cinnamon_count=Squirrel.objects.filter(Primary_Fur_Color="Cinnamon").count()
    Black_count=Squirrel.objects.filter(Primary_Fur_Color="Black").count()
    Ground_count=Squirrel.objects.filter(Location="Ground Plane").count()
    Above_count=Squirrel.objects.filter(Location="Above Ground").count()
    context = {
            'Total': Total,
            'Adult_count': Adult_count,
            'Juvenile_count': Juvenile_count,
            'Gray_count': Gray_count,
            'Cinnamon_count': Cinnamon_count,
            'Black_count': Black_count,
            'Ground_count': Ground_count,
            'Above_count': Above_count,
            }
    return render(request, 'squirrel/stats.html', context)








# Create your views here.
