from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class createSection(ModelForm):
	class Meta:
		model = section
		fields = ['section_id']

class createStudent(ModelForm):
	class Meta:
		model=student
		fields=['student_name','student_id','student_mail']

class book(ModelForm):
	class Meta:
		model=resource_booking
		fields=['select_booking','select_resource','quantity']

class bookLab(ModelForm):
	#startDate = forms.DateTimeField(required=True, input_formats = ["%Y-%m-%dT%H:%M", ])
	#lastDate = forms.DateTimeField(required=True, input_formats = ["%Y-%m-%dT%H:%M", ])
	class Meta:
		model = booking
		fields = ['section_id']
