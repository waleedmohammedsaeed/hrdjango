import pandas as pd
from django.core.management.base import BaseCommand
from hr.models import Specialization
from django.conf import settings
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        data_dir = os.path.join(settings.BASE_DIR, 'exceldata')
        csv_file = os.path.join(data_dir, 'ranks.csv')
        try:
            df = pd.read_csv(csv_file, encoding='windows-1256')
            # df['enamel'] = df['enamel'].fillna(value="waleed"),
            # df['job'] = df['job'].fillna(value="wale"),
            # df['active'] = df['active'].fillna(value=0),
            # df['salary'] = df['salary'].fillna(value=0),
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Cannot read data'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error reading'))

        for _,row in df.iterrows():
            Specialization.objects.create(
                spName = row['spName'],
            )
        self.stdout.write(self.style.SUCCESS('completed suucessfuly with no errors'))
        return

