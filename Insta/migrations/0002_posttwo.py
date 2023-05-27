# Generated by Django 4.1 on 2023-05-21 04:18

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("Insta", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostTwo",
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
                ("title", models.TextField(blank=True, null=True)),
                (
                    "image",
                    imagekit.models.fields.ProcessedImageField(
                        blank=True, null=True, upload_to="static/images/posts"
                    ),
                ),
            ],
        ),
    ]
