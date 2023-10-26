from django import forms
from .models import ChronologicalRecord

class ChronologicalRecordForm(forms.ModelForm):
    class Meta:
        model = ChronologicalRecord
        fields = ['title', 'content']