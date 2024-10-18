from django import forms

class ClassDiagram(forms.Form):
    className = forms.CharField(max_length = 200) 
    attribute = forms.CharField(max_length = 200) 
    method = forms.CharField(max_length = 200)