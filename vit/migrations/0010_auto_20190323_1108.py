# Generated by Django 2.1.7 on 2019-03-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vit', '0009_auto_20190323_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomdetails',
            name='fees',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
