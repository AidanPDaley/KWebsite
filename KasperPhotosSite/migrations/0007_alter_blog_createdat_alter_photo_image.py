# Generated by Django 4.1.4 on 2022-12-12 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KasperPhotosSite', '0006_blog_image_alter_blog_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 21, 48, 17, 278298, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]