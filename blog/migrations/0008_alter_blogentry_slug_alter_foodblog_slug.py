# Generated by Django 4.1.3 on 2022-12-12 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_blogentry_slug_alter_foodblog_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogentry",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name="foodblog",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
