from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from quiz.models import Answer, Option, Question, Questionare


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


class AnswerInlineAdmin(admin.TabularInline):
    model = Option
    ordering = ["-right", "answer__text"]
    extra = 3
    min_num = 2
    formset = AnswerInlineFormSet


class QuestionareInlineAdmin(admin.TabularInline):
    verbose_name = "набор тестов"
    verbose_name_plural = "наборы тестов"
    model = Questionare.questions.through


class HasOwnerFilter(admin.SimpleListFilter):
    title = "Включен в набор тестов"
    parameter_name = "has_owner"

    def lookups(self, request, model_admin):
        return (
            ("has_owner", "Да"),
            ("has_no_owner", "Нет"),
        )

    def queryset(self, request, queryset):
        if self.value() == "has_owner":
            return queryset.exclude(owner=None)
        if self.value() == "has_no_owner":
            return queryset.filter(owner=None)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["text"]
    search_help_text = "Поиск по тексту вопроса"
    list_display = ["text"]
    list_filter = [HasOwnerFilter]
    fields = ["text"]
    inlines = [AnswerInlineAdmin, QuestionareInlineAdmin]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["text"]


@admin.register(Questionare)
class QuestionareAdmin(admin.ModelAdmin):
    list_display = ["name"]
    filter_horizontal = ["questions"]
    ordering = ["name"]
