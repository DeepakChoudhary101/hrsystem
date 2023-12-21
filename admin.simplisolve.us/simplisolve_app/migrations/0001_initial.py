# Generated by Django 5.0 on 2023-12-20 07:18

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                ("otp", models.PositiveIntegerField(blank=True, null=True)),
                ("submitted", models.BooleanField(default=False)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("application_count", models.PositiveIntegerField(default=0)),
                ("last_application_date", models.DateTimeField(blank=True, null=True)),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                (
                    "experience_fields",
                    models.CharField(
                        choices=[
                            ("Python", "Python"),
                            ("R", "R"),
                            ("Statistics", "Statistics"),
                            ("All of the above", "All of the above"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "predictive_model_experience",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("1-3", "1-3"),
                            ("4-6", "4-6"),
                            ("7-9", "7-9"),
                            ("10+", "10+"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "data_visualization_experience",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("1-3", "1-3"),
                            ("4-6", "4-6"),
                            ("7-9", "7-9"),
                            ("10+", "10+"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "visa_sponsorship",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField(default="", max_length=1000)),
                ("application_count", models.PositiveIntegerField(default=0)),
                ("otp", models.PositiveIntegerField(blank=True, null=True)),
                ("submitted", models.BooleanField(default=False)),
                (
                    "last_application_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Data_scientist_data",
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
                ("id1", models.CharField(default="", max_length=500)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                ("otp", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "experience_fields",
                    models.CharField(
                        choices=[
                            ("Python", "Python"),
                            ("R", "R"),
                            ("Statistics", "Statistics"),
                            ("All of the above", "All of the above"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "predictive_model_experience",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("1-3", "1-3"),
                            ("4-6", "4-6"),
                            ("7-9", "7-9"),
                            ("10+", "10+"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "data_visualization_experience",
                    models.CharField(
                        choices=[
                            ("0", "0"),
                            ("1-3", "1-3"),
                            ("4-6", "4-6"),
                            ("7-9", "7-9"),
                            ("10+", "10+"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "visa_sponsorship",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DestinationModel",
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
                ("id1", models.CharField(default="", max_length=20)),
                ("first_name", models.CharField(default="", max_length=100)),
                ("post", models.CharField(max_length=40, null=True)),
                ("last_name", models.CharField(blank=True, default="", max_length=100)),
                ("email", models.EmailField(default="", max_length=254)),
                ("code", models.CharField(default="", max_length=20)),
                ("phone_number", models.CharField(default="", max_length=20)),
                (
                    "resume",
                    models.FileField(default="", upload_to="destination_resumes/"),
                ),
                ("datetime", models.DateTimeField(default=django.utils.timezone.now)),
                ("country_name", models.CharField(default="", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Interview",
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
                ("id1", models.CharField(default="", max_length=20)),
                ("post", models.CharField(max_length=40, null=True)),
                ("first_name", models.CharField(default="", max_length=100)),
                ("last_name", models.CharField(blank=True, default="", max_length=100)),
                ("email", models.EmailField(default="", max_length=254)),
                ("phone_number", models.CharField(default="", max_length=20)),
                (
                    "resume",
                    models.FileField(default="", upload_to="interview_resumes/"),
                ),
                ("datetime", models.DateTimeField(default=django.utils.timezone.now)),
                ("review", models.CharField(default="", max_length=500)),
                ("salary", models.CharField(default="", max_length=10)),
                ("is_rejected", models.BooleanField(default=False)),
                ("country_name", models.CharField(default="", max_length=50)),
                ("code", models.CharField(default="", max_length=50)),
                (
                    "rejection_reason",
                    models.TextField(default=" ", max_length=1000, null=True),
                ),
                ("meeting_link", models.URLField(default="", max_length=500)),
                ("interview_dates", models.DateField(blank=True, null=True)),
                (
                    "calendly_embed_code",
                    models.CharField(
                        default="https://calendly.com/dpkchoudhary103/interview",
                        max_length=500,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InterviewDateCoding",
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
                ("id1", models.CharField(default="", max_length=20)),
                ("selected_date_1", models.DateTimeField(blank=True, null=True)),
                ("selected_date_2", models.DateTimeField(blank=True, null=True)),
                ("selected_date_3", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="InterviewDateTechnical",
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
                ("id1", models.CharField(default="", max_length=20)),
                ("selected_date_1", models.DateTimeField(blank=True, null=True)),
                ("selected_date_2", models.DateTimeField(blank=True, null=True)),
                ("selected_date_3", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Machine_learning_engineer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                ("otp", models.PositiveIntegerField(blank=True, null=True)),
                ("submitted", models.BooleanField(default=False)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("application_count", models.PositiveIntegerField(default=0)),
                ("last_application_date", models.DateTimeField(blank=True, null=True)),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                (
                    "experience_generative_models",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "experience_ml_pipelines",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "preferred_work_location",
                    models.CharField(
                        choices=[
                            ("remote", "I d like to work remotely"),
                            ("onsite", "I d prefer to work onsite"),
                            ("hybrid", "I d prefer to work in a hybrid fashion"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Machine_learning_engineer_data",
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
                ("id1", models.CharField(default="", max_length=500)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "experience_generative_models",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "experience_ml_pipelines",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "preferred_work_location",
                    models.CharField(
                        choices=[
                            ("remote", "I d like to work remotely"),
                            ("onsite", "I d prefer to work onsite"),
                            ("hybrid", "I d prefer to work in a hybrid fashion"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("question_text", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="RejectionModel",
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
                ("id1", models.CharField(default="", max_length=20)),
                ("first_name", models.CharField(default="", max_length=100)),
                ("last_name", models.CharField(blank=True, default="", max_length=100)),
                ("email", models.CharField(default="", max_length=100)),
                ("resume", models.FileField(default="", upload_to="rejection_resume/")),
                ("datetime", models.DateTimeField(default=django.utils.timezone.now)),
                ("country_name", models.CharField(default="", max_length=100)),
                ("code", models.CharField(default="", max_length=20)),
                (
                    "rejection_reason",
                    models.TextField(default=" ", max_length=1000, null=True),
                ),
                (
                    "reject_by",
                    models.TextField(default=" ", max_length=1000, null=True),
                ),
                ("phone_number", models.CharField(default="", max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Research_scientist",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes_data_scientist/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                ("otp", models.PositiveIntegerField(blank=True, null=True)),
                ("submitted", models.BooleanField(default=False)),
                ("application_count", models.PositiveIntegerField(default=0)),
                ("last_application_date", models.DateTimeField(blank=True, null=True)),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "like_working_in_team",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "experience_with_ml_framework",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "research_publications",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "experience_as_research_scientist",
                    models.CharField(
                        choices=[
                            ("<1", "Less than a year"),
                            ("1-2", "1 - 2 years"),
                            ("2-4", "2 - 4 years"),
                            ("4-7", "4 - 7 years"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Research_scientist_Data",
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
                ("id1", models.CharField(default="", max_length=20)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes_data_scientist/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "like_working_in_team",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "experience_with_ml_framework",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "research_publications",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "experience_as_research_scientist",
                    models.CharField(
                        choices=[
                            ("<1", "Less than a year"),
                            ("1-2", "1 - 2 years"),
                            ("2-4", "2 - 4 years"),
                            ("4-7", "4 - 7 years"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Score_coding",
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
                ("id1", models.CharField(default="", max_length=10)),
                ("candidate", models.CharField(default="", max_length=50)),
                ("question_1", models.TextField(default="")),
                ("arafat_score_1", models.PositiveIntegerField(blank=True, null=True)),
                ("helal_score_1", models.PositiveIntegerField(blank=True, null=True)),
                ("mujib_score_1", models.PositiveIntegerField(blank=True, null=True)),
                ("question_2", models.TextField(default="")),
                ("arafat_score_2", models.PositiveIntegerField(blank=True, null=True)),
                ("helal_score_2", models.PositiveIntegerField(blank=True, null=True)),
                ("mujib_score_2", models.PositiveIntegerField(blank=True, null=True)),
                ("question_3", models.TextField(default="")),
                ("arafat_score_3", models.PositiveIntegerField(blank=True, null=True)),
                ("helal_score_3", models.PositiveIntegerField(blank=True, null=True)),
                ("mujib_score_3", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Score_technical",
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
                ("id1", models.CharField(default="", max_length=10)),
                ("candidate", models.CharField(default="", max_length=50)),
                ("question_1", models.TextField(default="")),
                ("arafat_score_1", models.PositiveIntegerField(blank=True, null=True)),
                ("helal_score_1", models.PositiveIntegerField(blank=True, null=True)),
                ("mujib_score_1", models.PositiveIntegerField(blank=True, null=True)),
                ("question_2", models.TextField(default="")),
                ("arafat_score_2", models.PositiveIntegerField(blank=True, null=True)),
                ("helal_score_2", models.PositiveIntegerField(blank=True, null=True)),
                ("mujib_score_2", models.PositiveIntegerField(blank=True, null=True)),
                ("question_3", models.TextField(default="")),
                ("arafat_score_3", models.PositiveIntegerField(blank=True, null=True)),
                ("helal_score_3", models.PositiveIntegerField(blank=True, null=True)),
                ("mujib_score_3", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Software_application_developer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                ("otp", models.PositiveIntegerField(blank=True, null=True)),
                ("submitted", models.BooleanField(default=False)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("application_count", models.PositiveIntegerField(default=0)),
                ("last_application_date", models.DateTimeField(blank=True, null=True)),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                ("project_link", models.URLField(blank=True, null=True)),
                (
                    "software_dev_experience",
                    models.CharField(
                        choices=[
                            ("<1", "Less than a year"),
                            ("1-2", "1 - 2 years"),
                            ("2-4", "2 - 4 years"),
                            ("4-7", "4 - 7 years"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "experience_with_sql",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "us_citizen_or_permanent_resident",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Software_application_developer_data",
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
                ("id1", models.CharField(default="", max_length=500)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(blank=True, default="", max_length=50)),
                ("country_code", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("resume", models.FileField(upload_to="resumes/")),
                ("datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("code", models.CharField(default="+1", max_length=20)),
                ("rejection_reason", models.TextField(max_length=1000, null=True)),
                (
                    "salary_exceptation",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("project_link", models.URLField(blank=True, null=True)),
                (
                    "software_dev_experience",
                    models.CharField(
                        choices=[
                            ("<1", "Less than a year"),
                            ("1-2", "1 - 2 years"),
                            ("2-4", "2 - 4 years"),
                            ("4-7", "4 - 7 years"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "experience_with_sql",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
                (
                    "us_citizen_or_permanent_resident",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")], max_length=3
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Marks",
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
                ("marks", models.IntegerField()),
                (
                    "interview",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="simplisolve_app.interview",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="simplisolve_app.question",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="question",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="simplisolve_app.topic"
            ),
        ),
        migrations.AddField(
            model_name="interview",
            name="topic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="simplisolve_app.topic",
            ),
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("new_notifications", models.PositiveIntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]