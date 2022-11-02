# Generated by Django 4.1.3 on 2022-11-02 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="company",
            name="employee",
        ),
        migrations.AddField(
            model_name="company",
            name="employee",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="company",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
