# Generated by Django 4.1.7 on 2023-07-02 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FYP_App', '0025_remove_student_session_year_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_subject',
            name='class_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FYP_App.class'),
            preserve_default=False,
        ),
    ]
