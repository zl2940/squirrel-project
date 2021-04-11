from django.core.management import BaseCommand,CommandError
import csv
import datetime
from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    def handle(self,*args,**options):
        path = options['path']
        with open(path, 'rt') as f:
            squirrel_info = csv.reader(f, dialect='excel')
            next(squirrel_info)
            id=list()
            for row in squirrel_info:
                if row[2] in id:
                    continue
                else:
                    id.append(row[2])
                    date = datetime.datetime.striptime(row[5],'m%d%Y')
                    squirrel = Squirrel.objects.create(
                        X=row[0],
                        Y=row[1],
                        Unique_Squirrel_ID=row[2],
                        Shift=row[4],
                        Date=date,
                        Age=row[7],
                        Primary_Fur_Color=row[8],
                        Location=row[12],
                        Specific_Location=row[14],
                        Running=(row[15]==True),
                        Chasing=(row[16]==True),
                        Climbing=(row[17]==True),
                        Eating=(row[18]==True),
                        Foraging=(row[19]==True),
                        Other_Activities=row[20],
                        Kuks=(row[21]==True),
                        Quaas=(row[22]==True),
                        Moans=(row[23]==True),
                        Tail_flags=(row[24]==True),
                        Tail_twitches=(row[25]==True),
                        Approaches=(row[26]==True),
                        Indifferent=(row[27]==True),
                        Runs_from=(row[28]==True),)


