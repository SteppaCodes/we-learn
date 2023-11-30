from django.forms import ValidationError
from django.core.validators import RegexValidator

def validate_name(value):
    if len(value.split()) > 1:
        raise ValidationError("No space between names")
    elif not value.isalpha():
        raise ValidationError("Name can contain only alphabets")
    return value 

alternate_validate_name = RegexValidator(
    regex=r"^[a-zA-Z]*$", message="No spaces between names"
)