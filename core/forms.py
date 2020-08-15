from django import forms
from core.models import Forms, Field, Option, Response

class FormsForm(forms.ModelForm):
    class Meta:
        model = Forms
        fields = ('title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg content-input', 'placeholder': 'Blank title'}),
            'description': forms.TextInput(attrs={'class': 'form-control content-input', 'placeholder': 'Form description'}),
        }

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('question', 'answer_type', 'is_required', )