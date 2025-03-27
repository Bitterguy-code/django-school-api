from django.db import models
from django.core.exceptions import ValidationError
from subject_app.validators import validate_professor_name, validate_subject_format

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(unique=True, validators=[validate_subject_format])
    professor = models.CharField(unique=False, validators=[validate_professor_name])
    
    def add_a_student(self, pk):
        error_message = "This subject is full!"
        if self.students.count() == 31:
            raise Exception(error_message)
        else:
            self.students.add(pk)
        
        
    def drop_a_student(self, pk):
        error_message = "This subject is empty!"
        if self.students.count() == 0:
            raise Exception(error_message)
        else:
            self.students.remove(pk)