from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from subject_app.models import Subject

from student_app.validators import validate_combination_format, validate_email_format, validate_name_format

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=255, unique=False, validators=[validate_name_format])
    student_email = models.EmailField(unique=True, validators=[validate_email_format])
    personal_email = models.EmailField(null=True, unique=True)
    locker_number = models.IntegerField(default=110, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(default='12-12-12', unique=False, validators=[validate_combination_format])
    good_student = models.BooleanField(default=True, unique=False)
    subjects = models.ManyToManyField(Subject, related_name='students', validators=[v.MinLengthValidator(1), v.MaxLengthValidator(8)])
    
    def add_subject(self, pk):
        error_message = "This students class schedule is full!"
        if self.subjects.count() == 8:
            raise Exception(error_message)
        else:
            self.subjects.add(pk)
        
    def remove_subject(self,pk):
        error_message = "This students class schedule is empty!"
        if self.subjects.count() == 0:
            raise Exception(error_message)
        else:
            self.subjects.remove(pk)
    
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self,new_locker):
        self.locker_number=new_locker
        
    def student_status(self, status):
        self.good_student=status