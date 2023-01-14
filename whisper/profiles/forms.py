from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Phone

class CustomUserCreationForm (UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'bg-light rounded-pill form-control px-0.5 text-dark', 'style': 'font-size: 0.75em;'})


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_number']
    
    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = 'Phone Number (eg. 123-456-7890)'
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control mb-1 bg-light rounded-pill form-control px-0.5 text-dark', 'style': 'font-size: 0.75em;'})
