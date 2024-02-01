from django import forms
from apps.models import Movie
class movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'