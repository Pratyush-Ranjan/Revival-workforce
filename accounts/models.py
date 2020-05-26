from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Company(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Companyname = models.CharField(max_length=50, blank=False)
    Phone_no = PhoneNumberField(blank=True, help_text='Contact Phone Number')
    Address = models.CharField(max_length=100, blank=False)
    Industry_type = models.CharField(max_length=50, blank=True)
    Skill_required = models.CharField(max_length=50, blank=False)