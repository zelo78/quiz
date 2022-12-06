from django.contrib import admin
from django.contrib.admin import TabularInline
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from quiz.models import Answer, Option, Question


class AnswerInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        right, wrong = 0, 0
        for form in self.forms:
            data = form.cleaned_data
            if data.get("answer"):
                if data.get("right") is True:
                    right += 1
                elif data.get("right") is False:
                    wrong += 1

        if right == 0:
            raise ValidationError("Нет правильного ответа")

        if wrong == 0:
            raise ValidationError("Нет неправильного ответа")


class AnswerInlineAdmin(TabularInline):
    model = Option
    ordering = ["-right", "answer__text"]
    extra = 3
    min_num = 2
    formset = AnswerInlineFormSet


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["text"]
    list_display = ["text"]
    fields = ["text"]
    inlines = [AnswerInlineAdmin]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["text"]
