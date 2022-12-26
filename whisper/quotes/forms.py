from django.forms import ModelForm
from .models import Quote
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['content', 'author', 'description', 'date', 'time']
        widgets = {
            'date': AdminDateWidget(),
            'time': AdminTimeWidget(),
        }