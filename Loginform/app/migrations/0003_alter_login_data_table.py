# Generated by Django 5.1.2 on 2024-11-05 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_login_login_data'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='login_data',
            table='login',
        ),
    ]
