from django.contrib.auth.models import User
from users.models import Profile
from input.models import *


def update_profile(user_list, text, action):	

	if action == 'Start':
		new_status = 2 
		current_task = text['task']
	elif action == 'End':
		new_status = 1
		current_task = 'None'
	elif action == 'Record':
		print("Recording ONLY")
	elif action == 'Break':
		new_status = 3
		current_task = 'Break'
	else:
		print("Action Mismatch")

	for member in user_list:
		profile = Profile.objects.filter(user = member).first()	
		profile.status = new_status
		profile.current_task = current_task
		profile.save()
	


def validate(form, request, update_status):
	action = "Error"
	if form.is_valid():
		post = form.save(commit = False)
		text = form.clean()
		print(text)
		
		post.user = get_user_by_username(text['user_name'])
		profile = Profile.objects.filter(user = post.user).first()
		user_list = [post.user]
		post.members = [post.user.pk]

		if profile.is_grp:
			group = Group.objects.get(grp_name = post.user)
			all_members = group.users.all()
			for member in all_members:
				user_list.append(member)
				post.members.append(member.pk)

		if update_status:
			if text['task'] == 'MYLBRK001':
				action = "Break"
			elif profile.status == 2:
				action = "End"
			else:
				action = "Start"
			update_profile(user_list, text, action)	
		else:
			action = "Record"

		post.action = action
		post.save()						
		return text
