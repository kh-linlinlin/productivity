from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


class Profile(models.Model):

	user = models.OneToOneField(User,  on_delete = models.CASCADE, related_name = 'auth_user')
	wms_id = models.IntegerField(default = 0, unique = True)
	is_grp = models.BooleanField(default = 0) # is_grp = 0: Individual, is_grp = 1: Group
	is_lead = models.BooleanField(default = 0) # 0: Agent, 1: Lead / Supervisor / WH Managers
	whs_id = models.CharField(max_length = 100, null = True)

	name =  models.CharField(max_length = 500, default = 'Default Name')
	default_function = models.CharField(max_length = 500, default = '')
	status = models.PositiveSmallIntegerField(default = 1) # status = 1 : IDLE, status = 2: In Task
	current_task = models.CharField(max_length = 500, default = 'None')
	current_grp = models.CharField(max_length = 500, default = 'Individual')
	ctime = models.DateTimeField(auto_now_add = True)
	mime = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f'{self.user.username}'




