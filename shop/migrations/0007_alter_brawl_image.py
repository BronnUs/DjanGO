# Generated by Django 4.2.2 on 2023-06-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_brawl_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brawl',
            name='image',
            field=models.ImageField(upload_to='django_lab/media/'),
        ),
    ]
