# Generated by Django 3.1.3 on 2020-11-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20201123_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='amount',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trade',
            name='price',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=64),
            preserve_default=False,
        ),
    ]
