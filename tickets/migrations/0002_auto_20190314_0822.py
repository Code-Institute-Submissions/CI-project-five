# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 08:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user_upvoted_list',
            field=models.ManyToManyField(related_name='upvoters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('DOING', 'Doing'), ('DONE', 'Done')], default='TO DO', max_length=20),
        ),
    ]
