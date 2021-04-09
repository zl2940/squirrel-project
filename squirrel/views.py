from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'squirrel/index.html',context))



# Create your views here.
