from django import forms
from app.models import list_item

class list_itemform(forms.ModelForm):
    class Meta:
        model = list_item
        fields = '__all__'