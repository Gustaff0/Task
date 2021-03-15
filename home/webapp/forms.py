from django import forms
from django.forms import widgets
from webapp.models import Status, Type

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Summary')
    description = forms.CharField(max_length=3000, label='Description', required=False, widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all())