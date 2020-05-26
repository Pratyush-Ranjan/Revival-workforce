from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.contrib.auth.models import 	User

# Create your models here.
class Worker(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=20, blank=False)
    Lastname = models.CharField(max_length=20, blank=False)
    Phone_no = PhoneNumberField(blank=True, help_text='Contact Phone Number')
    Address = models.CharField(max_length=100, blank=False)
    Industry = models.CharField(max_length=50, blank=True)
    Skill = models.CharField(max_length=50, blank=False)
    aadhaar_regex = RegexValidator(regex=r'^\d{4}\s\d{4}\s\d{4}$', message="Aadhaar number must be entered in the format: 'XXXX XXXX XXXX'.")
    Aadhaar = models.CharField(validators=[aadhaar_regex], max_length=14, blank=False)
    pan_regex = RegexValidator(regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', message="Pan number must be entered in the format: 'XXXXX9999X'.( Where X ia alphabetic character and 9 is numerical digit)")
    PAN = models.CharField(validators=[pan_regex], max_length=10, blank=True)