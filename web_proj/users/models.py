from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	wms_id = models.PositiveIntegerField()
	name =  models.CharField(max_length = 500, default = 'blank')
	default_grp = models.CharField(max_length = 500, default = 'Individual')
	default_fn = models.CharField(max_length = 500, default = '')
	status = models.PositiveSmallIntegerField(default = 1)
	ctime = models.DateTimeField(auto_now_add = True)
	mime = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f'{self.user.username} Profile'


