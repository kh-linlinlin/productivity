from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	wms_id = models.PositiveIntegerField()
	task = models.CharField(max_length = 100)
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True) 
