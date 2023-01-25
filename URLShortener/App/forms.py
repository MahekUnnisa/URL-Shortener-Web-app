from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	password = forms.PasswordInput(required=True)

	class Meta:
		model = User
		fields = ("full_name", "occupation", "phone_number", "email", "password", "confirm_password")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.password = self.cleaned_data['password']
		if commit:
			user.save()
		return user