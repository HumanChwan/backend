# Generated by Django 4.0.5 on 2022-09-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
