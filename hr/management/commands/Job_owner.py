import pandas as pd
from django.core.management.base import BaseCommand
from hr.models import Job_owner
from django.conf import settings
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        data_dir = os.path.join(settings.BASE_DIR, 'exceldata')
        csv_file = os.path.join(data_dir, 'job_owner.csv')
        try:
            df = pd.read_csv(csv_file, encoding='windows-1256')
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading {e}'))
            print(e)

        for _,row in df.iterrows():
            Job_owner.objects.create(
                Job_owner_name = row['job_owner'],
            )
        self.stdout.write(self.style.SUCCESS('completed suucessfuly with no errors'))
        return

