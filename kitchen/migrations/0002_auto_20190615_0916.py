# Generated by Django 2.2.2 on 2019-06-15 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderstransit',
            old_name='dish_id',
            new_name='dish',
        ),
        migrations.RenameField(
            model_name='orderstransit',
            old_name='order_id',
            new_name='order',
        ),
    ]
