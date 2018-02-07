from django import forms
 
class PostForm(forms.Form):
    name = forms.CharField(max_length=256)
    password = forms.DateTimeField()
