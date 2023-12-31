# Generated by Django 4.2.1 on 2023-06-20 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('release_year', models.DateField()),
                ('available', models.BooleanField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.company')),
            ],
        ),
    ]
