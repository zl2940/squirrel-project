from django.core.management import BaseCommand, CommandError
import csv
from squirrel.models import Squirrel

class Command(BaseCommand):
    help='Export Squirrel Data'
    def add_arguments(self, parser):
        parser.add_argument('path',type=str)
    def handle(self, *args,**kwargs):
        path = kwargs['path']
        from django.apps import apps
        Squirrel_M = apps.get_model('squirrel', 'Squirrel')
        name = [n.name for n in Squirrel_M._meta.fields]
        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(name)
            for squirrel in Squirrel_M.objects.all():
                writer.writerow([getattr(squirrel,n) for n in name])

