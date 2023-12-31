# Generated by Django 5.0 on 2023-12-20 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("simplisolve_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interview",
            name="topic",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="simplisolve_app.topic",
            ),
        ),
    ]
