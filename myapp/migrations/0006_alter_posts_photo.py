# Generated by Django 5.0.3 on 2024-06-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_categories_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='photo',
            field=models.ImageField(default='/img/', upload_to='img/'),
        ),
    ]
