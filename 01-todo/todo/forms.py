from django import forms
from .models import TodoItem

class TodoForm(forms.ModelForm):
    """
    A form to create and edit TodoItem instances.
    """
    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'due_date', 'resolved']
        widgets = {
            # Use the DateInput widget for a better date picker experience
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
