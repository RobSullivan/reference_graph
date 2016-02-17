from django import forms


class PMIDForm(forms.Form):
    pmid = forms.CharField(max_length=30, label='PMID')
