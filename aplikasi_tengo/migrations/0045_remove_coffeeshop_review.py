# Generated by Django 5.1.1 on 2024-09-13 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi_tengo', '0044_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeeshop',
            name='review',
        ),
    ]
