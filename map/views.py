from django.shortcuts import render
from django.shortcuts import get_object_or_404

from squirrel.models import Squirrel

def map(request):
    squirrel_p= Squirrel.objects.all()[:100]

	context = {
		'postions': squirrel_p,
	}
	return render(request, 'map/map.html', context)
# Create your views here.
