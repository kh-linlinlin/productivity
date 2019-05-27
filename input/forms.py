from django import forms
from input.models import Post
from django.contrib.auth.models import User 
task_list = ['Picking', 'Packing', 'Receiving', 'QC', 'Bundling', 'Putaway']

class ActionForm(forms.ModelForm):
	user_name = forms.CharField()
	task = forms.CharField(required = False)
	work_complete = forms.CharField(required = False)
	
	class Meta:
		model = Post
		fields = ('user_name', 'task', 'work_complete')

	def clean(self):
		if self.cleaned_data['task'] not in task_list:
			raise forms.ValidationError("This task is not valid. Please scan again!")
		return self.cleaned_data  


class GroupForm(forms.ModelForm):
	member_name = forms.CharField(label = '')

	class Meta:
		model = Post
		fields = ('member_name', )