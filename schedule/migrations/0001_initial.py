# Generated by Django 4.1.7 on 2023-03-11 07:44

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth_module", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DateRange",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("start_date_time", models.DateTimeField()),
                ("end_date_time", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                ("slot_selection_minute_multiplier", models.IntegerField()),
                ("slot_book_minute_width", models.IntegerField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_module.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Label",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#99e4ff", image_field=None, max_length=18, samples=None
                    ),
                ),
                ("keterangan", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                (
                    "datetime_range",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.daterange",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schedule.event"
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="schedule.label",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "ID",
                    models.CharField(
                        auto_created=True,
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=30, null=True)),
                (
                    "schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.schedule",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_module.user",
                    ),
                ),
            ],
        ),
    ]
