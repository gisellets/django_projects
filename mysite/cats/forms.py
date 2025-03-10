from django import forms

class CatForm(forms.Form):
    text = forms.CharField(max_length=200)

class TypesForm(forms.Form):
    text = forms.CharField(max_length=200)
