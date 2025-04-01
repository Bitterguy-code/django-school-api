# Generated by Django 5.1.7 on 2025-03-29 00:58

import django.core.validators
import student_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject_app', '0002_alter_subject_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[student_app.validators.validate_name_format])),
                ('student_email', models.EmailField(max_length=254, unique=True, validators=[student_app.validators.validate_email_format])),
                ('personal_email', models.EmailField(max_length=254, null=True, unique=True)),
                ('locker_number', models.IntegerField(default=110, unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)])),
                ('locker_combination', models.CharField(default='12-12-12', validators=[student_app.validators.validate_combination_format])),
                ('good_student', models.BooleanField(default=True)),
                ('subjects', models.ManyToManyField(related_name='students', to='subject_app.subject')),
            ],
        ),
    ]
