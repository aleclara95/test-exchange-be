# Generated by Django 3.1.3 on 2020-11-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201120_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=5, default=1, max_digits=64),
            preserve_default=False,
        ),
    ]
