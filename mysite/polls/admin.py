from django.contrib import admin

from .models import Question

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        # The first value is the name of the set
        # it will display on the admin page
        # as a section header
        ("Date Information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
