from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields = ('original_link', 'custom_string', 'expiration_date')