from django import forms

class CatForm(forms.Form):
    text = forms.CharField(max_length=200)
