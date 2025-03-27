# Generated by Django 5.1.7 on 2025-03-26 22:48

import subject_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(unique=True, validators=[subject_app.validators.validate_subject_format])),
                ('professor', models.CharField(unique=True, validators=[subject_app.validators.validate_professor_name])),
            ],
        ),
    ]
