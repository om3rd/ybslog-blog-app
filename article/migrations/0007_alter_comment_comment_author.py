# Generated by Django 4.1 on 2023-04-04 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0006_alter_comment_comment_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment_author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Comment",
            ),
        ),
    ]
