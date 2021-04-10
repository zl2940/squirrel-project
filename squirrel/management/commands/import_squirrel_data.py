from django.core.management import BaseCommand
import csv
from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel data'
