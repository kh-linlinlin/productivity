from django import forms
from input.models import Post
from django.contrib.auth.models import User 


class UserForm(forms.ModelForm):
	user_name = forms.CharField()
	task = forms.CharField(required = True)
	work_complete = forms.CharField(initial = '', required = True)

	class Meta:
		model = Post
		fields = ('user_name', 'task', 'work_complete')




class GroupForm(forms.ModelForm):
	member_name = forms.CharField()

	class Meta:
		model = Post
		fields = ('member_name', )