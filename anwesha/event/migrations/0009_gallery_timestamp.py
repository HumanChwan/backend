# Generated by Django 4.1 on 2022-10-28 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_remove_gallery_element_gallery_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
