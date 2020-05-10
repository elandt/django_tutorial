import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


# Extends the Model class of models
class Question(models.Model):
    # these class variables are a database field,
    # and their names are the column names
    # CharFields require max_length is provided
    question_text = models.CharField(max_length=200)
    # the optional first positional arg to a Field is
    # a "human-readable" column name
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # These attributes need to come after the method definition
    # They provide Django with info about how
    # to display the result of the method on the admin page
    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # default is an optional keyward arg
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
