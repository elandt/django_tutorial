from django.contrib import admin

from .models import Choice, Question

# Register your models here.


class ChoiceInLine(admin.StackedInline):
    model = Choice
    # Provide enough fields for 3
    # choices when editing choices on
    # the Question admin page in addition to
    # the fields for choices that exist
    # for the Question already
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        # The first value is the name of the set
        # it will display on the admin page
        # as a section header
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]})
    ]
    # Adds the ChoiceInLine class to the QuestionAdmin page
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
