# Generated by Django 4.1.3 on 2022-12-06 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="option",
            name="answer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="quiz.answer",
                verbose_name="ответ",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="options",
            field=models.ManyToManyField(
                through="quiz.Option", to="quiz.answer", verbose_name="ответ"
            ),
        ),
        migrations.CreateModel(
            name="Questionare",
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
                ("name", models.CharField(max_length=64, verbose_name="наименование")),
                (
                    "questions",
                    models.ManyToManyField(
                        related_name="owner", to="quiz.question", verbose_name="вопросы"
                    ),
                ),
            ],
            options={
                "verbose_name": "набор тестов",
                "verbose_name_plural": "наборы тестов",
            },
        ),
    ]