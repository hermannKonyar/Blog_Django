# Generated by Django 4.1.3 on 2022-12-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_alter_blogentry_image_alter_foodblog_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
            ],
        ),
    ]
