# Generated by Django 2.2.14 on 2020-08-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_photos_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]