# Generated by Django 5.0.4 on 2024-04-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('publish_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
