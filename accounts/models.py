from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE = [
        (1, 'المكلف'),
        (2, 'مدير الموارد البشرية'),
        (3, 'مدير الوحدة'),
    ]
    role = models.SmallIntegerField(choices=ROLE, default=3)

    def __str__(self):
        return self.first_name