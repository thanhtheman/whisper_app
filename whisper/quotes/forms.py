from django.forms import ModelForm
from .models import Quote
from django import forms

class QuoteForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3, "placeholder": "please write something my friend"}))
    class Meta:
        model = Quote
        fields = ['owner','content', 'author', 'description', 'date', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)