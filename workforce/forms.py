from django import forms
from .models import Worker

class WorkerCreateForm(forms.ModelForm):
	class Meta:
		model = Worker
		fields = ('Firstname','Lastname','Phone_no','Address','Industry','Skill','Aadhaar','PAN')