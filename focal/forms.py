from django import forms
from .models import Mission
class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['title', 'content']
        labels = {'title': 'Title', 'content': 'Content'}