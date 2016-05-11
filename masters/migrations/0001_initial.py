# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-05 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='Email address')),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('date_left', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('city', models.CharField(max_length=20)),
                ('postcode', models.CharField(max_length=5, verbose_name='Post Code')),
                ('state', models.CharField(max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('line1', models.CharField(default='-', max_length=30)),
                ('line2', models.CharField(default='-', max_length=30)),
                ('line3', models.CharField(default='-', max_length=30)),
            ],
            options={
                'ordering': ['first_name'],
                'verbose_name_plural': 'adult',
            },
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('gender', models.CharField(choices=[('B', 'Boy'), ('G', 'Girl')], max_length=1, verbose_name='Gender')),
                ('mobile_no', models.CharField(max_length=15, verbose_name='Mobile no.')),
                ('email', models.CharField(blank=True, max_length=30, verbose_name='Email address')),
                ('date_joined', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['first_name'],
                'verbose_name_plural': 'kid',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.BooleanField(default=True, verbose_name='Children')),
                ('adult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.Adult')),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.Kid')),
            ],
        ),
        migrations.AddField(
            model_name='adult',
            name='members',
            field=models.ManyToManyField(through='masters.Membership', to='masters.Kid'),
        ),
    ]
