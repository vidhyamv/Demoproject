# Generated by Django 3.2.7 on 2021-09-29 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='Cartitem',
        ),
    ]