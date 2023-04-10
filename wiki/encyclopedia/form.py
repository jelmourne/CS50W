from django import forms
from . import util

class createEntry(forms.Form):
    title = forms.CharField(max_length="50", empty_value=False)

    content = forms.CharField(widget=forms.Textarea(attrs={"rows":2,"cols":5}),empty_value=False)

class editEntry(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Use Markdown Language','rows':2,'cols':5}),empty_value=None)