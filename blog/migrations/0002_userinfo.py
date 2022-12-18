# Generated by Django 4.1.3 on 2022-12-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("name", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("isActive", models.BooleanField()),
            ],
        ),
    ]
