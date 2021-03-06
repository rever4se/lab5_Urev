# Generated by Django 3.1.4 on 2020-12-27 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('country', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Card_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('accuracy_date', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('finish_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('person', models.CharField(max_length=45)),
            ],
        ),
    ]
