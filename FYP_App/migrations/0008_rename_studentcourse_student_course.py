# Generated by Django 4.1.7 on 2023-06-25 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FYP_App', '0007_rename_student_d_student_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Studentcourse',
            new_name='Student_Course',
        ),
    ]