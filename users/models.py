from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE )
	date_joined = models.DateTimeField(default=timezone.now)
	profile_pic = models.ImageField(default="profile_pics/default.jpg", upload_to="profile_pics")
	about_me = models.TextField()

	def __str__(self):
		return f'{self.user.username} Profile'
