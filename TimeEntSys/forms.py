from django import forms
from django.forms import ModelForm
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Task Name', required=True,
           widget=forms.TextInput(attrs={
                                           "class": "form-control",
                                           "pattern": "[ .a-zA-Z]+",
                                           "size": "50",
                                           "style": "font-size: medium",
                                           "Placeholder": "Enter the task",
                                           "id": "name",
                                        }
                                 )
                          )
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    duration = forms.CharField(label='Time duration', required=True,
               widget=forms.TextInput(attrs={
                                              "class": "form-control",
                                              "pattern": "[ .a-zA-Z]+",
                                              "size": "50",
                                              "style": "font-size: medium",
                                              "Placeholder": "Enter the task",
                                              "id": "name",  
                                            }
                                     )
                              )
    class Meta:
        model = Task
        fields = (
                    "project",
                    "name",
                    "start_time",
                    "end_time",
                    "duration"
                 )