from django.forms import ModelForm
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
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
        self.fields['first_name'].validators.append(
            RegexValidator(
                regex='^[a-zA-Z]',
                message='Only alphabets, numbers, - and _ are allowed for usernames and your username must start with an alphabet.',
                code='invalid_firstname',
            )
        )
        self.fields['last_name'].validators.append(
            RegexValidator(
                regex='^[a-zA-Z]',
                message='Only alphabets, numbers, - and _ are allowed for usernames and your username must start with an alphabet.',
                code='invalid_lastname',
            )
        )
       
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.fields['sex'].required = True
        self.fields['birth_date'].required = True
        self.fields['bloodtype'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password', 'birth_date', 'sex', 'bloodtype']
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
            },
            'bloodtype': {
                'required': 'Blood type is required'
            }
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email = cleaned_data.get('email')
        # email must be unique
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'That email address is already in use')
        return cleaned_data


class UpdateProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        # there's a 'fields' property now
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'sex', 'bloodtype']

    def clean(self):
        cleaned_data = super(UpdateProfileForm, self).clean()
        return cleaned_data
    
       


class calculate_bmiForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(calculate_bmiForm, self).__init__(*args, **kwargs)
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
        cleaned_data = super(calculate_bmiForm, self).clean()
        return cleaned_data


class calculate_dciForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(calculate_dciForm, self).__init__(*args, **kwargs)
        self.fields['useractivity'].required = True

    class Meta:
        model = User
        fields = ['useractivity']
        error_messages = {
            'useractivity': {
                'required': 'User Activity is required'
            }
        }

    def clean(self):
        cleaned_data = super(calculate_dciForm, self).clean()
        return cleaned_data
