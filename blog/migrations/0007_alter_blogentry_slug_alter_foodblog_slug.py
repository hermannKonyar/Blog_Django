# Generated by Django 4.1.3 on 2022-12-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blogentry_video_foodblog_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogentry",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="foodblog",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
