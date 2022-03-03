from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Car(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	photo = models.ImageField(upload_to='cars')
	seller = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('ads-home'
		# kwargs={'pk': self.pk}
		)
