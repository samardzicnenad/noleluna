# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('state', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=1)),
                ('tags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'Luna Samardzic'), (2, 'Novak Samardzic'), (3, 'Svetlana Samardzic'), (4, 'Nenad Samardzic'), (5, 'Samardzic Family')], max_length=9, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Blog Posts',
                'verbose_name': 'Blog Post',
            },
        ),
    ]
