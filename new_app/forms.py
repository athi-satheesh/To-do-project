import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.forms import models
from new_app.models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    class Meta:
        model = Todo
        fields = ('title', 'name', 'date')

