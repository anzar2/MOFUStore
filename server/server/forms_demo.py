from django.forms import (
    CharField,
    PasswordInput,
    TextInput,
    EmailInput,
    IntegerField,
    NumberInput,
    ChoiceField,
    Select,
    ImageField,
    Form
)

class FormImageDemo(Form):
    image = ImageField()