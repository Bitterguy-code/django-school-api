from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, default='default')
    student_email = models.EmailField(default='default@default.com')
    personal_email = models.EmailField(null=True)
    locker_number = models.IntegerField(default=1)
    locker_combination = models.CharField(default='default')
    good_student = models.BooleanField(default=True)