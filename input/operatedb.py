from django.contrib.auth.models import User
from users.models import Profile
from input.models import *


def update_profile(user, text, action):
	profile = Profile.objects.filter(user = user).first()
	if action == 'Start':
		profile.status = 2 
		profile.current_task = text['task']
	elif action == 'End':
		profile.status = 1
		profile.current_task = 'None'
	else:
		print("Action Mismatch!")
	profile.save()
	


def validate(form, request):

	if form.is_valid():
		post = form.save(commit = False)
		text = form.cleaned_data
		
		post.user = get_user_by_username(text['user_name'])
		profile = Profile.objects.filter(user = post.user).first()
		if profile.status == 2:
			action = "End"
			msg = text['user_name'] + " ends task"
		elif profile.status == 1:
			action = "Start"
			msg = text['user_name'] +" starts task: " + text['task'] + " at "
		post.save()
		update_profile(post.user, text, action)
		return msg
