# Generated by Django 5.0 on 2023-12-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("simplisolve_app", "0002_alter_interview_topic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Save_score_data_scientist_technical",
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
                ("id1", models.CharField(default="", max_length=100)),
                ("topic", models.CharField(default="", max_length=100)),
                ("question1", models.CharField(default="", max_length=100)),
                ("marks1", models.PositiveIntegerField(blank=True, null=True)),
                ("question2", models.CharField(default="", max_length=100)),
                ("marks2", models.PositiveIntegerField(blank=True, null=True)),
                ("question3", models.CharField(default="", max_length=100)),
                ("marks3", models.PositiveIntegerField(blank=True, null=True)),
                ("question4", models.CharField(default="", max_length=100)),
                ("marks4", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
