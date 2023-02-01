from django.forms import ModelForm
from .models import Quote
from django import forms

class QuoteForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3, "placeholder": "why do you like this quote?"}))
    class Meta:
        model = Quote
        fields = ['title', 'content', 'author', 'date_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = 'Quote/Video-link/Goal'
        self.fields['date_time'].label = 'Pick Date & Time (EST)'
        for name, field in self.fields.items():
            if field.label == 'Pick Date & Time (EST)':
                field.widget.attrs.update({'class': 'form-control form-control-lg mb-1', 'id':'datetimepicker'})
            field.widget.attrs.update({'class': 'form-control mb-1'})