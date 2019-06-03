from django import forms
from input.models import Post, Task
from django.contrib.auth.models import User 
import json
from django.core.serializers.json import DjangoJSONEncoder


class ActionForm(forms.ModelForm):
	user_name = forms.CharField()
	task = forms.CharField(required = False)
	work_complete = forms.CharField(required = False)
	
	class Meta:
		model = Post
		fields = ('user_name', 'task', 'work_complete')

	def clean(self):
		self.cleaned_data['task'].capitalize()
		self.cleaned_data['work_complete'].capitalize()
		print(self.cleaned_data['task'])

		tasks_queryset = Task.objects.all().values('task_code')
		task_list = json.dumps(list(tasks_queryset), cls = DjangoJSONEncoder)
		

		if self.cleaned_data['task'] not in task_list:
			raise forms.ValidationError("This task is not valid. Please scan again!")
		return self.cleaned_data    


class GroupForm(forms.ModelForm):
	member_name = forms.CharField(label = '')

	class Meta:
		model = Post
		fields = ('member_name', )