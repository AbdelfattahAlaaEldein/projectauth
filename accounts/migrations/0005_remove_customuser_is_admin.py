# Generated by Django 5.0.4 on 2024-05-16 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
    ]
