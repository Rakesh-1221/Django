from django import forms
from app.models import login_data


class loginform(forms.ModelForm):
    class Meta:
        model = login_data
        fields = "__all__"


class checkform(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=20)
