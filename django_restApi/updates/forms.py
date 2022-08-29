from django import forms
from .models import Update
class ModelUpdateForm(forms.ModelForm):
	class Meta:
		model = Update
		fields = [
				'id',
				'user',
				'content',
				'image',
		]
	def clean(self, *args, **kwargs):
		data = self.cleaned_data
		content = data.get('content', None)
		image = data.get('image', None)
		if content == '':
			content = None
		if content is None and image is None:
			raise forms.ValidationError('All Fields are required.')
		return super().clean(*args, **kwargs)
