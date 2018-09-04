from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


@admin.register(Question)
class QuestionDisplay(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # (None, {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceDisplay(admin.ModelAdmin):
    # list_display = ('choice_text', 'question', 'votes')
    fieldsets = [
        (None, {'fields': ['choice_text']}),
        (None, {'fields': ['votes'], 'classes': ['collapse']}),
    ]