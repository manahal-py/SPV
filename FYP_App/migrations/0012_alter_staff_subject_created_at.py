# Generated by Django 4.1.7 on 2023-06-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYP_App', '0011_alter_staff_subject_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
