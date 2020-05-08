# This can be used to replace the HttpResponse
# and template loader
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


# Create your views here.
class IndexView(generic.ListView):
    # Overriding the the ListView generic view default
    # template called <app name>/<model name>_list.html
    template_name = "polls/index.html"
    # Override the automatically generated context variable is question_list
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five pulished questions (not
        including those set to be published in the
        future).
        """
        now = timezone.now()
        order = "-pub_date"
        # __lte filters for pub_date less than or equal
        # to the provided value
        return Question.objects.filter(pub_date__lte=now).order_by(order)[:5]


class DetailView(generic.DetailView):
    model = Question
    # Overrides the default template name of DetailView
    # generic, default is <app name>/<model name>_detail.html
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object, values are always strings
        # request.POST["choice"] will raise KeyError
        # if choice wasn't provided in POST data
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        url_redirect = "polls:results"
        return HttpResponseRedirect(reverse(url_redirect, args=(question_id,)))
