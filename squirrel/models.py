from django.db import models

from django.utils.translation import gettext as 


class Squirrel(models.Models):
    X = models.DecimalField(
            max_length=100,
            help_text=_('Longitude'),
            blank=True,
            )

    Y = models.DecimalField(
            max_length=100,
            help_text=_('Latitude'),
            blank=True,
            )

    Unique_Squirrel_ID = models.Charfield(
            max_length=100,
            help_text=_('Unique Squirrel ID'),
            )

    AM='AM'
    PM='PM'
    TIME_CHOICE = [
            (AM,_('AM')),
            (PM,_('PM')),
            ]
    Shift = models.CharField(
            max_length=15,
            help_text=_('Shifting time'),
            choices=TIME_CHOICE,
            blank=True,
            )

    Date = models.DateField(
            help_text=_('Specific date'),
            )

    ADULT='Adult'
    JUVENILE='Juvenile'
    AGE_CHOICE = [
            (ADULT,_('Adult')),
            (JUVENIL,_('Juvenile')),
            ]
    Age = models.CharField(
            max_length=15,
            help_text=_('Age of Squirrel'),
            choices=AGE_CHOICE,
            blank=True,
            )

    GREY='Grey'
    CINNAMON='Cinnamon'
    BLACK='Black'
    COLOR_CHOICES = [
            (GREY,_('Grey')),
            (CINNAMON,_('Cinnamon')),
            (BLACK,_('Black')),
            ]
    Primary_Fur_Color = models.CharField(
            max_length=15,
            help_text=_('Primary fur color of the squirrel'),
            choices=COLOR_CHOICE,
            blank=True,
            )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = [
            (GROUND_PLANE,_('Ground Plane')),
            (ABOVE_GROUND,_('Above Ground')),
            ]
     Location = models.CharField(
            max_length=30,
            help_text=_('sighter instructed squirrel location'),
            choices=LOCATION_CHOICES,
            blank=True,
            )

     Specific_Location = models.CharField(
             max_length=100,
             help_text=_('Specific location of the squirrel'),
             blank=True,
             )

     Running = models.BooleanField(
             max_length=15,
             help_text=_('Is it running'),
             default=False,
             )

     Chasing = models.BooleanField(
             max_length=15,
             help_text=_('Is it chasing'),
             default=False,
             )

     Climbing = models.BooleanField(
             max_length=15,
             help_text=_('Is it climbing'),
             default=False,
             )

     Eating = models.BooleanField(
             max_length=15,
             help_text=_('Is it eating'),
             default=False,
             )

     Foraging = models.BooleanField(
             max_length=15,
             help_text=_('Is it foraging'),
             default=False,
             )

     Other_Activities = models.CharField(
             max_length=100,
             help_text=_('Specific activity the squirrel is doing'),
             blank=True,
             )

     Kuks = models.BooleanField(
             max_length=15,
             help_text=_('Whether kuks'),
             default=False,
             )

     Quaas = models.BooleanField(
             max_length=15,
             help_text=_('Whether quaas'),
             default=False,
             )

     Moans = models.BooleanField(
             max_length=15,
             help_text=_('Whether moans'),
             default=False,
             )

     Tail_flags = models.BooleanField(
             max_length=15,
             help_text=_('Whether tail flags'),
             default=False,
             )

     Tail_twitches = models.BooleanField(
             max_length=15,
             help_text=_('Whether tail twitches'),
             default=False,
             )

     Approaches = models.BooleanField(
             max_length=15,
             help_text=_('Whether approaching to human being'),
             default=False,
             )

     Indifferent = models.BooleanField(
             max_length=15,
             help_text=_('Whether showing indifferent to human being'),
             default=False,
             )

     Runs_from = models.BooleanField(
             max_length=15,
             help_text=_('Whether runing from human being'),
             default=False,
             )

     def __str__(self):
         return self.Unique_Squirrel_ID








# Create your models here.
