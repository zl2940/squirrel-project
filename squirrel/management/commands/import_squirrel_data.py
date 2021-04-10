from django.core.management import BaseCommand,CommandError
import csv
from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    def handle(self,*args,**options):
        path = options['path']
        with open(path, 'r') as f:
            squirrel_info = csv.reader(f, dialect='excel')
            for row in squirrel_info:
                squirrel = Squirrel.objects.create(
                        Latitude=row[0]
                        Longitude=row[1]
                        Unique_Squirrel_ID=row[2]
                        Shift=row[3]
                        Date=row[4]
                        Age=row[5]
                        Primary_Fur_Color=row[6]
                        Location=row[7]
                        Specific_Location=row[8]
                        Running=row[9]
                        Chasing=row[10]
                        Climbing=row[11]
                        Eating=row[12]
                        Foraging=row[13]
                        Other_Activities=row[14]
                        Kuks=row[15]
                        Quaas=row[16]
                        Moans=row[17]
                        Tail_flags=row[18]
                        Tail_twitches=row[19]
                        Approaches=row[20]
                        Indifferent=row[21]
                        Runs_from=row[22])


