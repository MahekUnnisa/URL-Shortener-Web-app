from django import forms
from .models import Link
from django.core.validators import URLValidator

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields = ['original_link', 'custom_string', 'expiration_date']

	def clean_original_link(self):
		original_link = self.cleaned_data['original_link']
		url_validator = URLValidator()
		try:
			url_validator(original_link)
		except:
			raise forms.ValidationError("Invalid URL")
		return original_link