# Generated by Django 4.1.4 on 2022-12-12 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KasperPhotosSite', '0004_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 6, 57, 12, 49643, tzinfo=datetime.timezone.utc)),
        ),
    ]
