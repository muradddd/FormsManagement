from django import forms
from core.models import Forms, Field, Option, Response

class FormsForm(forms.ModelForm):
    class Meta:
        model = Forms
        fields = ('title', 'description',)

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('question', 'answer_type', 'is_required', )