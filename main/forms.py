from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['native', 'translation', 'script', 'native_info', 'translation_info']
        widgets = {
            'script': forms.HiddenInput(),
        }
