from django import forms
from .models import Link
# Create your forms here.

class LinkForm(forms.ModelForm):
	class Meta:
		model = Link
		fields = ('original_link', 'custom_string', 'expiration_date')