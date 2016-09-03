from django import forms

class CandidatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    partido = forms.CharField(max_length=4)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)