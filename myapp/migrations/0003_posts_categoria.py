# Generated by Django 5.0.3 on 2024-06-12 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_posts_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.categories'),
        ),
    ]