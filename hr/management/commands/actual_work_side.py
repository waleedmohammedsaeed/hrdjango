import pandas as pd
from django.core.management.base import BaseCommand
from hr.models import Actual_work_side, Actual_work_area
from django.conf import settings
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        data_dir = os.path.join(settings.BASE_DIR, 'exceldata')
        csv_file = os.path.join(data_dir, 'actual_work_side.csv')
        try:
            df = pd.read_csv(csv_file, encoding='windows-1256')
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading {e}'))
            print(e)

        for _,row in df.iterrows():
            awa = Actual_work_area.objects.get(id=1)
            Actual_work_side.objects.create(
                actual_work_side_name = row['actual_work_side'],
                actual_work_area = awa,
            )
        self.stdout.write(self.style.SUCCESS('completed suucessfuly with no errors'))
        return

