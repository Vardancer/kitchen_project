# Generated by Django 2.2.2 on 2019-06-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_auto_20190615_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
