from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
	user_name = models.CharField(max_length = 100)
	task = models.CharField(max_length = 100)
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True) 
	work_complete = models.CharField(max_length = 100)
	action = models.CharField(max_length = 100)
	members = models.TextField() # list of pk of User object
	ctime = models.DateTimeField(auto_now = True)

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

class Task(models.Model):

	TASK_CHOICES = (
		('IB', 'Inbound'),
		('OB', 'Outbound'),
		('INV', 'Inventory'),
		('UN', 'Unspecified'),
		('BK', 'Break')
	)

	WHS_CHOICES = (
		('MYL', 'MYL'),
		('THA', 'THA'), 
		('VNN', 'VNN'),
		('UN', 'Unspecified'),
	)

	task_code = models.CharField(max_length = 100)
	whs_id = models.CharField(max_length = 3, choices = WHS_CHOICES, default = 'UN')
	category = models.CharField(max_length  = 3, choices = TASK_CHOICES, default = 'UN')
	task_name = models.TextField()
	output_record = models.BooleanField(default = 0)

	
