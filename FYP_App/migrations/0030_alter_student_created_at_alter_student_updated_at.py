# Generated by Django 4.1.7 on 2023-07-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYP_App', '0029_remove_staff_subject_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]