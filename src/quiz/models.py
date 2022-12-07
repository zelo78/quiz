from django.db import models


class Answer(models.Model):
    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"
        ordering = ["text"]

    text = models.CharField("текст ответа", max_length=100, unique=True)

    def __str__(self):
        return f"{self.text}"

    def clean(self):
        self.text = self.text.strip()


class Question(models.Model):
    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"
        ordering = ["text"]

    text = models.TextField("текст вопроса")
    options = models.ManyToManyField(Answer, verbose_name="ответ", through="Option")

    def __str__(self):
        return f"{self.text}"

    def clean(self):
        self.text = self.text.strip()


class Option(models.Model):
    class Meta:
        verbose_name = "вариант ответа"
        verbose_name_plural = "варианты ответов"
        unique_together = ["question", "answer"]

    question = models.ForeignKey(
        Question, verbose_name="вопрос", on_delete=models.CASCADE
    )
    answer = models.ForeignKey(Answer, verbose_name="ответ", on_delete=models.CASCADE)
    right = models.BooleanField("правильность", default=False)

    def __str__(self):
        return f"{'Правильный' if self.right else 'Неправильный'} ответ '{self.answer.text}'"


class Questionare(models.Model):
    class Meta:
        verbose_name = "набор тестов"
        verbose_name_plural = "наборы тестов"
        ordering = ["name"]

    name = models.CharField("наименование", max_length=64)
    questions = models.ManyToManyField(
        Question,
        verbose_name="вопросы",
        related_name="owner",
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"
