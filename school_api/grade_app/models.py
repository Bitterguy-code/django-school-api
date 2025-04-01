from django.db import models
from django.core import validators as v
from subject_app.models import Subject
from student_app.models import Student

# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(
        default = 100,
        decimal_places=2,
        max_digits=5,
        blank = False,
        null = False,
        validators=[v.MinValueValidator(0.00), v.MaxValueValidator(100.00)])
    a_subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.a_subject} - {self.student.name} - {self.grade}"