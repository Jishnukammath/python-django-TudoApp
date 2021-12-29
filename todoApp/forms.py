from .models import Task
from django import forms
class Tudoforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']