from django import forms

class SpellingForm(forms.Form) :
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
