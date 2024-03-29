# Generated by Django 4.0.7 on 2022-10-14 14:26

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name="Country",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название страны"),
                ),
                (
                    "alpha2code",
                    models.CharField(
                        max_length=2, unique=True, verbose_name="ISO Alpha2"
                    ),
                ),
                (
                    "alpha3code",
                    models.CharField(max_length=3, verbose_name="ISO Alpha3"),
                ),
                ("capital", models.CharField(max_length=50, verbose_name="Столица")),
                ("region", models.CharField(max_length=50, verbose_name="Регион")),
                (
                    "subregion",
                    models.CharField(max_length=50, verbose_name="Субрегион"),
                ),
                ("population", models.IntegerField(verbose_name="Население")),
                ("latitude", models.FloatField(verbose_name="Широта")),
                ("longitude", models.FloatField(verbose_name="Долгота")),
                (
                    "demonym",
                    models.CharField(
                        help_text="Название жителей",
                        max_length=50,
                        verbose_name="Демоним",
                    ),
                ),
                ("area", models.FloatField(verbose_name="Площадь")),
                (
                    "numeric_code",
                    models.CharField(
                        help_text="ISO 3166-1 numeric",
                        max_length=3,
                        validators=[
                            django.core.validators.MinLengthValidator(limit_value=3)
                        ],
                        verbose_name="Трёхзначный код страны",
                    ),
                ),
                ("flag", models.CharField(max_length=255, verbose_name="Флаг")),
                (
                    "currencies",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=3),
                        size=None,
                        verbose_name="Валюты",
                    ),
                ),
                (
                    "languages",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=20),
                        size=None,
                        verbose_name="Языки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Страна",
                "verbose_name_plural": "Страны",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="City",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Название города"),
                ),
                ("region", models.CharField(max_length=50, verbose_name="Регион")),
                ("latitude", models.FloatField(verbose_name="Широта")),
                ("longitude", models.FloatField(verbose_name="Долгота")),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="country",
                        to="geo.country",
                        verbose_name="Страна",
                    ),
                ),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
                "ordering": ["name"],
            },
        ),
    ]
