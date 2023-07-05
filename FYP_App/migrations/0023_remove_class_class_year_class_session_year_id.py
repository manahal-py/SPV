# Generated by Django 4.1.7 on 2023-06-30 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FYP_App', '0022_student_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='class_year',
        ),
        migrations.AddField(
            model_name='class',
            name='session_year_id',
            field=models.ForeignKey(default='2019', on_delete=django.db.models.deletion.DO_NOTHING, to='FYP_App.session_year'),
            preserve_default=False,
        ),
    ]