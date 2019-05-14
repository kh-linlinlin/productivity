from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Action(models.Model):
	title = models.CharField(max_length = 100)
	from_status = models.TextField()
	to_status = models.TextField()
	date_action = models.DateTimeField(default = timezone.now) 
	author = models.ForeignKey(User, on_delete = models.PROTECT)

	def __str__(self):
		return self.title