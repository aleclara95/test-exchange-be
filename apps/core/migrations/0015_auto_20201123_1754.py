# Generated by Django 3.1.3 on 2020-11-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20201122_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='amount',
            field=models.DecimalField(decimal_places=5, max_digits=64, null=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=64, null=True),
        ),
    ]
