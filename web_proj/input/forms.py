from django import forms
from input.models import Post

class ScanForm(forms.ModelForm):
	## fields in one form
	wms_id = forms.IntegerField()
	task = forms.CharField()

	class Meta:
		model = Post 
		fields = ('wms_id', 'task')