# Generated by Django 4.1.3 on 2022-12-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_videos"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodblog",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]