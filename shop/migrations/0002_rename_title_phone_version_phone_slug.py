# Generated by Django 4.2.1 on 2023-06-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='title',
            new_name='version',
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
