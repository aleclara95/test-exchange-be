# Generated by Django 3.1.3 on 2020-11-19 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201119_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
