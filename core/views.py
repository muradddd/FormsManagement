from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import FormMixin
from core.forms import FormsForm, FieldForm
from core.models import Forms, Field, Option,Response, ResponseQA


class HomePageView(FormMixin, TemplateView):
    template_name = "index.html"
    form_class = FormsForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formsForm"] = FormsForm
        context["fieldForm"] = FieldForm
        return context

# Create your views here.
