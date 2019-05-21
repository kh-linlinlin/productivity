from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	user_name = models.CharField(max_length = 100)
	task = models.CharField(max_length = 100)
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True) 
	ctime = models.DateTimeField(auto_now = True)
	work_complete = models.CharField(max_length = 100)


def get_user_by_username(username):
	return User.objects.filter(username = username).first()


class Group(models.Model):

	users = models.ManyToManyField(User)
	curr_grp = models.ForeignKey(User, related_name = "curr_grp", null = True, on_delete = models.DO_NOTHING)
	ctime = models.DateTimeField(auto_now_add = True)
	mtime = models.DateTimeField(auto_now = True)

	@classmethod
	def add_member(cls, curr_grp, new_member):
		group, created = cls.objects.get_or_create(
			curr_grp = curr_grp
		)
		group.users.add(new_member)


	@classmethod
	def remove_member(cls, curr_grp, curr_member):
		group, created = cls.objects.get_or_create(
			curr_grp = curr_grp
		)
		group.users.remove(curr_member)
		

# class Group_modification(models.Model):
	