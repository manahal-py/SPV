# Generated by Django 4.1.7 on 2023-06-25 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FYP_App', '0006_student_d_studentcourse_d'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_d',
            new_name='Student',
        ),
        migrations.RenameModel(
            old_name='Studentcourse_d',
            new_name='Studentcourse',
        ),
    ]
