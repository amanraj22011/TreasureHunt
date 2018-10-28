from django import forms
from .models import TreasureGram

class TreasureForm(forms.ModelForm):
    class Meta:
        model = TreasureGram
        fields = {'name', 'value', 'meterial', 'location', 'image_url'}