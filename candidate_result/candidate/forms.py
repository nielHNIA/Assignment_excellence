from django import forms
from .models import *


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"
