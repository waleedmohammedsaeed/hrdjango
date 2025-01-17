from django.db import models

# Create your models here.

class Eclass(models.Model):
    className = models.CharField(max_length=50)

    def __str__(self):
        return self.className

    class Meta:
        verbose_name = 'Eclass'
        verbose_name_plural = 'Eclasses'

class Nationality(models.Model):
    nationality_name = models.CharField(max_length=50)

    def __str__(self):
        return self.nationality_name

    class Meta:
        verbose_name = 'Nationality'
        verbose_name_plural = 'Nationalities'


class Job(models.Model):
    jobName = models.CharField(max_length=50)

    def __str__(self):
        return self.jobName

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

class Specialization(models.Model):
    spName = models.CharField(max_length=60)

    def __str__(self):
        return self.spName

    class Meta:
        verbose_name = 'Specialization'
        verbose_name_plural = 'Specializations'

class GeneralSpecialization(models.Model):
    gsName = models.CharField(max_length=60)

    def __str__(self):
        return self.gsName

    class Meta:
        verbose_name = 'GeneralSpecialization'
        verbose_name_plural = 'GeneralSpecializations'

class Area_side(models.Model):
    area_side_name = models.CharField(max_length=75)

    def __str__(self):
        return self.area_side_name

class Actions(models.Model):
    action_name = models.CharField(max_length=50)

    def __str__(self):
        return self.action_name
    
#----------------------------------------------------------------
class Actual_work_area(models.Model):
    actual_work_area_name = models.CharField(max_length=50)

    def __str__(self):
        return self.actual_work_area_name

class Actual_work_side(models.Model):
    actual_work_side_name = models.CharField(max_length=200)
    actual_work_area = models.ForeignKey(Actual_work_area, on_delete=models.CASCADE)

    def __str__(self):
        return self.actual_work_side_name
    
class Job_owner(models.Model):
    Job_owner_name = models.CharField(max_length=60)

    def __str__(self):
        return self.Job_owner_name


class Administrator_side(models.Model):
    admin_name = models.CharField(max_length=80)

    def __str__(self):
        return self.admin_name

class Employee(models.Model):
    JOB_TYPES = [
        (1, "خدمة مدنية"),
        (2, "تشغيل ذاتي"),
    ]

    EMPTYPE = [
        (1, "Employee"),
        (2, "SOP")
    ]
    SEX = [
        (1, "ذكر"),
        (2, "انثي"),
    ]

    emptype = models.IntegerField(choices=EMPTYPE, null=True, blank=True)
    jobtype = models.IntegerField(choices=JOB_TYPES, null=True, blank=True)
    identity = models.IntegerField(null=True, blank=True)
    eclass = models.ForeignKey(Eclass, on_delete=models.CASCADE, related_name="eclass", null=True, blank=True)
    empno = models.BigIntegerField()
    ename = models.CharField(max_length=75)
    telNo = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, related_name="nationality", null=True, blank=True)
    sex = models.IntegerField(choices=SEX, null=True, blank=True)
    bdate = models.DateField(null=True, blank=True)
    job_title = models.ForeignKey(Job,  on_delete=models.CASCADE, null=True, blank=True)
    rank = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name="specialization", null=True, blank=True)
    general_specialization = models.ForeignKey(GeneralSpecialization, on_delete=models.CASCADE, related_name="generalspecialization", null=True, blank=True)
    job_id = models.CharField(max_length=20, null=True, blank=True)
    job_owner = models.ForeignKey(Job_owner, on_delete=models.CASCADE)
    owner_side = models.CharField(max_length=75, null=True, blank=True)
    actual_work_area = models.ForeignKey(Actual_work_area, on_delete=models.CASCADE)
    actual_work_side = models.ForeignKey(Actual_work_side, on_delete=models.CASCADE)
    area_side_type = models.ForeignKey(Area_side, on_delete=models.CASCADE, null=True, blank=True)
    adminstrator = models.ForeignKey(Administrator_side, on_delete=models.CASCADE)
    lastAction_date = models.CharField(max_length=20, null=True, blank=True)
    last_action = models.ForeignKey(Actions, on_delete=models.CASCADE, null=True, blank=True)
    manager_name = models.CharField(max_length=75, null=True, blank=True)
    hire_date = models.CharField(max_length=20, null=True, blank=True)
    ministry_attachment = models.CharField(max_length=20, null=True, blank=True)
    country_attachement_date = models.CharField(max_length=20, null=True, blank=True)
    owner_status = models.CharField(max_length=75, null=True, blank=True)
    service_type = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.ename

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    # @property
    # def hiredate(self):
    #     gregorian_date = self.hire_date
    #     hijri_date = islamic.from_gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day)
    #     return f"{hijri_date[2]}-{hijri_date[1]}-{hijri_date[0]}"
    #
    # @property
    # def country_attachment(self):
    #     gregorian_date = self.country_attachement_date
    #     hijri_date = islamic.from_gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day)
    #     return f"{hijri_date[2]}-{hijri_date[1]}-{hijri_date[0]}"

