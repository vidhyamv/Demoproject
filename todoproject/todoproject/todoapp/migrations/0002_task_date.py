# Generated by Django 3.2.7 on 2021-09-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-03-19'),
            preserve_default=False,
        ),
    ]