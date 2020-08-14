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

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            created_by = request.user
            form = Forms(title=title, description=description, created_by=created_by)
            form.save()
            field_count = request.POST.get('fieldCount')
            for i in range(int(field_count)+1):
                question = request.POST.get(f'fieldIndex-{i}-question')
                answer_type = request.POST.get(f'fieldIndex-{i}-answer_type')
                is_required = request.POST.get(f'fieldIndex-{i}-is_required')
                if is_required:
                    is_required = True
                else:
                    is_required = False
                field = Field(form=form, question=question, answer_type=answer_type, is_required=is_required)
                field.save()
        
        return redirect(reverse_lazy('core:form-detail', kwargs={'pk': form.pk}))


class FormDetailView(FormMixin, DetailView):
    model = Forms
    template_name = "form-detail.html"
    form_class = FormsForm

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_object()
            answered_by = request.user
            response = Response(form=form, answered_by=answered_by)
            response.save()
            field_count = request.POST.get('fieldCount')
            for i in range(int(field_count)):
                question = request.POST.get(f'question-{i}')
                answer = request.POST.get(f'answer-{i}')
                response_qa = ResponseQA(response=response, question=question, answer=answer)
                response_qa.save()
        
        return redirect(reverse_lazy('core:form-detail', kwargs={'pk': self.get_object().pk}))

class FormListView(ListView):
    model = Forms
    template_name = "form-list.html"


class ResponseListView(ListView):
    model = Response
    template_name = "response-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.request.GET.get('form')
        if form:
            context['responses'] = Response.objects.filter(form=form)
        else:
            context['responses'] = Response.objects.all()
        return context