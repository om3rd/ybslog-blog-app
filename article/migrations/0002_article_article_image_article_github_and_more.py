# Generated by Django 4.1 on 2023-03-09 18:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="article_image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="",
                verbose_name="Add photo into article",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="github",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="article",
            name="linkedin",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]