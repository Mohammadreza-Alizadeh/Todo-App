from django import forms
from django.forms import ModelForm

from .models import Task
    
class AddTaskForm(ModelForm):
    class Meta:
        model = Task    
        fields = ['task_name', 'task_description', 'task_priority']
        widgets = {
        'task_name':forms.TextInput(attrs={
            'class' : 'form-control',
            'style': 'color : #fff'
            }),

        'task_description': forms.Textarea(attrs={
            'class' : 'form-control',
            'style': 'color : #fff'
            }),

        'task_priority' : forms.Select(attrs={
            'class' : 'form-select text-white',
            'style': 'background: #343a40; border : 3px solid #7e0606'
        })


        }



class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task    
        fields = ['task_name', 'task_description', 'task_priority']
        widgets = {
        'task_name':forms.TextInput(attrs={
            'class' : 'form-control',
            'style': 'color : #fff'
            }),

        'task_description': forms.Textarea(attrs={
            'class' : 'form-control',
            'style': 'color : #fff'
            }),

        'task_priority' : forms.Select(attrs={
            'class' : 'form-select text-white',
            'style': 'background: #343a40; border : 3px solid #7e0606'
        })

        }
