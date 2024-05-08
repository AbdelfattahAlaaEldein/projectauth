from django.db import models

# Create your models here.
# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_password_strength(value):
    if len(value) < 8:
        raise ValidationError(_('Password must be at least 8 characters long.'), code='password_too_short')
    if not any(char.isdigit() for char in value):
        raise ValidationError(_('Password must contain at least one digit.'), code='password_no_digit')
    if not any(char.isalpha() for char in value):
        raise ValidationError(_('Password must contain at least one letter.'), code='password_no_letter')
    if value.islower():
        raise ValidationError(_('Password must contain at least one uppercase letter.'), code='password_no_uppercase')
    if value.isupper():
        raise ValidationError(_('Password must contain at least one lowercase letter.'), code='password_no_lowercase')
    if not any(char.isalnum() for char in value):
        raise ValidationError(_('Password must contain at least one alphanumeric character.'), code='password_no_alphanumeric')
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=12)
    password = models.CharField(_('password'), max_length=128, validators=[validate_password_strength])

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
    




class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    phone_number = models.CharField(max_length=15, blank=True)






