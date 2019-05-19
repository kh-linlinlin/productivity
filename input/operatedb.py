from django.contrib.auth.models import User
from users.models import Profile
from input.models import Group

def get_user_by_username(username):
	return User.objects.filter(username = username).first()


def update_profile(user, text, action):
	profile = Profile.objects.filter(user = user).first()
	if action == 'Start':
		profile.status = 2 
		profile.current_task = text['task']
	elif action == 'End':
		profile.status = 1
		profile.current_task = ''
	else:
		print("Action Mismatch!")
	profile.save()
	


def validate(form, request, action):

	if form.is_valid():
		post = form.save(commit = False)
		text = form.cleaned_data

		if action == 'Start' and text['user_name']:
			post.user = get_user_by_username(text['user_name'])
		else:
			post.user = request.user

		profile = Profile.objects.filter(user = post.user).first()
		if profile.status == 2 and action == 'Start':
			text = "You are currently in other task"
		elif profile.status == 1 and action == 'End':
			text = "You are currently at IDLE status"
		else:
			post.save()
			update_profile(post.user, text, action)
		return text

def get_member_list(user):
	profile = Profile.objects.filter(user = user).first()
	if profile.is_grp == 0:
		return None
	else:
	    group = Group.objects.get(curr_grp = user)
	    all_members = group.users.all()
	    return all_members