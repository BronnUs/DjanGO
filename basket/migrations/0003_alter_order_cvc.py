# Generated by Django 4.2.1 on 2023-06-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_remove_basket_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='CVC',
            field=models.IntegerField(),
        ),
    ]
