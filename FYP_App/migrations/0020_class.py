# Generated by Django 4.1.7 on 2023-06-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYP_App', '0019_auto_20230627_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('session_id', models.IntegerField(max_length=4)),
            ],
        ),
    ]