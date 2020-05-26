from django import forms
from django.forms import ValidationError
from .models import Company

class UserRegistrationForm(forms.Form):
	username = forms.CharField(
			required = True,
			label = 'Username',
			max_length = 32
		)
	email = forms.EmailField(
			required = True,
			label = 'Email',
			max_length = 32,
		)
	password = forms.CharField(
			required = True,
			label='Password', 
			max_length = 32,
			widget=forms.PasswordInput()
		)
	password2 = forms.CharField(
			required = True,
			label='Repeat Password', 
			max_length = 32,
			widget=forms.PasswordInput()
		)
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password']!=cd['password2']:
			raise forms.ValidationError("passwords don't match")
		return cd['password2']


class CompanyRequirementForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('Name','Companyname','Phone_no','Address','Industry_type','Skill_required')