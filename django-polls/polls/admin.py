from django.contrib import admin

from .models import Choice, Question

# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    # By default, provide enough fields for 3
    # choices when editing choices on
    # the Question admin page in addition to
    # the fields for choices that exist
    # for the Question already
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # By default, Django displays the str() of each object
    # This can be overridden by telling Django what
    # what to display for an object using list_display
    list_display = ("question_text", "pub_date", "was_published_recently")
    # Adds a filter on the pub_date to the Question selection admin page
    # The type of filter displayed depends on the type of field being filtered
    list_filter = ["pub_date"]
    # Adds the ability to search the Question selection
    # admin page by question_text
    # Searching uses a LIKE in the query behind the scenes
    search_fields = ["question_text"]
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
