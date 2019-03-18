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
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['sex'].required = True
        self.fields['birth_date'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'birth_date', 'sex']
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
            'sex': {
                'required': 'Sex is required'
            }
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email = cleaned_data.get('email')
        # email must be unique
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'That email address is already in use')
        return cleaned_data


class CalculateBMIForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CalculateBMIForm, self).__init__(*args, **kwargs)
        self.fields['height'].required = True
        self.fields['weight'].required = True

    class Meta:
        model = User
        fields = ['height', 'weight']
        error_messages = {
            'height': {
                'required': 'Height is required'
            },
            'weight': {
                'required': 'Weight is required'
            },
        }

    def clean(self):
        cleaned_data = super(CalculateBMIForm, self).clean()
        return cleaned_data
class CalculateDCIForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CalculateDCIForm, self).__init__(*args, **kwargs)
        self.fields['useractivity'].required = True

    class Meta:
        fields = ['useractivity']
        error_messages = {
            'useractivity':{
                'required': 'User Activity is required'
            }
        }

    def clean(self):
        cleaned_data = super(CalculateDCIForm, self).clean()
        return cleaned_data
