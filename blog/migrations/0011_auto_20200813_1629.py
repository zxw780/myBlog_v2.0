# Generated by Django 2.2.14 on 2020-08-13 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_gallery_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='album_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Gallery'),
        ),
    ]