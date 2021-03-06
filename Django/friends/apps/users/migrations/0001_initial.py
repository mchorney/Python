# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-27 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password_hash', models.CharField(max_length=255)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friends', models.ManyToManyField(through='users.Friendship', to='users.User')),
            ],
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_a', to='users.User'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_b', to='users.User'),
        ),
    ]
