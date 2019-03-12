from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import User


class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # there's a 'fields' property now
        self.fields['username'].validators.append(
            RegexValidator(
                regex='^[a-zA-Z][a-zA-Z0-9_-]+$',
                message='Only alphabets, numbers, - and _ are allowed for usernames and your username must start with an alphabet.',
                code='invalid_username',
            )
        )
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'birth_date', 'height', 'weight', 'age']
        error_messages = {
            'first_name': {
                'required': 'First name is required'
            },
            'last_name': {
                'required': 'Last name is required'
            },
            'username': {
                'required': 'Username is required'
            },
            'email': {
                'required': 'Email address is required'
            },
            'password': {
                'required': 'Password is required'
            },
            'birth_date': {
                'required': 'Birth date is required'
            },
            'height': {
                'required': 'Height is required'
            },
            'weight': {
                'required': 'Weight is required'
            },
            'age': {
                'required': 'Age is required'
            }
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email = cleaned_data.get('email')
        # email must be unique
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'That email address is already in use')
        return cleaned_data
