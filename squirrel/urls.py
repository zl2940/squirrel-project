from django.urls import path

from . import views

urlpatterns = [
        path('',views.sightings, name='sightings'),
        path('create/',views.create, name='create'),
        path('stats/',views.stats, name='stats'),
        path('<str:Unique_Squirrel_ID>/',views.update,name='update'), 
]

