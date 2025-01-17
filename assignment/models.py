from django.db import models

class New_assignment(models.Model):
    ASS_STATE = [
        (0, 'refused'),
        (1, 'start'),
        (2, 'approved'),
        (3, 'clearenced'),
        (4, 'assigned to'),
        (5, 'finished'),
    ]
    employee = models.ForeignKey('hr.Employee', on_delete=models.CASCADE)
    decision_no = models.CharField(max_length=30)
    decision_start_date = models.DateField()
    current_work = models.CharField(max_length=200)
    new_work = models.ForeignKey('hr.Actual_work_side', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)
    state = models.SmallIntegerField(choices=ASS_STATE, default=1, blank=True, null=True)
    startwork = models.DateField()
    def __str__(self):
        return self.employee.ename + '-' + self.current_work

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

# Create your models here.
