from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm (UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'bg-light rounded-pill form-control px-0.5 text-dark', 'style': 'font-size: 0.75em;'})