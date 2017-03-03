from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):

	class Meta:
		model = User
		fields = ['username','password','email']