import pandas as pd
from django.core.management.base import BaseCommand
from hr.models import Employee, Eclass, Nationality, Job, Specialization, GeneralSpecialization, Area_side, Actions, Actual_work_area, Actual_work_side, Job_owner, Administrator_side
from django.conf import settings
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        data_dir = os.path.join(settings.BASE_DIR, 'exceldata')
        csv_file = os.path.join(data_dir, 'emp.csv')
        try:
            df = pd.read_csv(csv_file, encoding='windows-1256')

            # df['enamel'] = df['enamel'].fillna(value="waleed"),
            # df['job'] = df['job'].fillna(value="wale"),
            # df['active'] = df['active'].fillna(value=0),
            # df['salary'] = df['salary'].fillna(value=0),
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Cannot read data'))
            return

        for _,row in df.iterrows():
            cl = Eclass.objects.get(id=row['eclass'])
            na = Nationality.objects.get(id=row['nationality'])
            jt = Job.objects.get(id=row['job_title'])
            rk = Specialization.objects.get(id=row['rank'])
            gs = GeneralSpecialization.objects.get(id=row['general_specialization'])
            ast = Area_side.objects.get(id=row['area_side_type'])
            la = Actions.objects.get(id=row['last_action'])

            awa = Actual_work_area.objects.get(id=row['actual_work_area'])
            aws = Actual_work_side.objects.get(id=row['actual_work_side'])
            jow = Job_owner.objects.get(id=row['job_owner'])
            asd = Administrator_side.objects.get(id=row['adminstrator'])
            
            Employee.objects.create(
                emptype = row['emptype'],
                jobtype  = row['jobtype'],
                identity = row['identity'],
                eclass = cl,
                empno = row['empno'],
                ename = row['ename'],
                telNo = row['telNo'],
                email = row['email'],
                nationality = na,
                sex = row['sex'],
                bdate = row['bdate'],
                job_title = jt,
                rank = rk,
                general_specialization = gs,
                job_id = row['job_id'],
                job_owner = jow,
                owner_side = row['owner_side'],
                actual_work_area = awa,
                actual_work_side = aws,
                area_side_type = ast,
                adminstrator = asd,
                lastAction_date = row['last_action_date'],
                last_action = la,
                manager_name = row['manager_name'],
                hire_date = row['hire_date'],
                ministry_attachment = row['ministry_attachment'],
                country_attachement_date = row['country_attachement_date'],
                owner_status = row['owner_status'],
                service_type = row['service_type'],
            )
        self.stdout.write(self.style.SUCCESS('completed suucessfuly with no errors'))
        return
        # return super().handle(*args, **options)

