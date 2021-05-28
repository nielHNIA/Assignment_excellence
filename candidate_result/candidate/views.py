from django.shortcuts import render
from candidate.models import *
from candidate.forms import *

from django.db.models import Avg, Max
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
"""def index(request):
    return render(request, 'candidate/index.html')
"""

class HomeView(TemplateView):
    template_name = "candidate/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["candidates"] = Candidate.objects.all()
        context["tests"] = Test.objects.all()



        max = 0
        max_candidate = 'a'
        """for candidate in Candidate.objects.all():
            for score in candidate.test_set.all():
                print(score.avg_scorer)
                if score.avg_scorer() > max:
                    max = score.avg_scorer()
                    max_candidate = score.name"""
        for score in Test.objects.all():
            #print(vars(score.avg_scorer[0]))
            if score.avg_scorer() > max:
                max = score.avg_scorer()
                max = round(max, 2)
                max_candidate = score.name
        context['max'] = max
        context['max_candidate'] = max_candidate

        return context

class NewCandidateView(CreateView):
    template_name = "candidate/add_candidate.html"
    model = Candidate
    form_class = CandidateForm

class CandidateView(ListView):
    template_name = "candidate/candidates.html"
    model = Candidate


class TestView(ListView):
    template_name = "candidate/tests.html"
    model = Test
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddTestView(CreateView):
    template_name = "candidate/add_test.html"
    model = Test

    form_class = TestForm



class UpdateTestView(UpdateView):
    template_name = "candidate/update_test.html"
    model = Test
    form_class = TestForm

class UpdateCandidateView(UpdateView):
    template_name = "candidate/update_candidate.html"
    model = Candidate
    form_class = CandidateForm
