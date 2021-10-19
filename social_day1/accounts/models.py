from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 200)
	content = models.TextField()
	image = models.ImageField(upload_to='post_pics', blank = True)
	file = models.FileField(upload_to='post_videos', blank = True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name = 'likes', blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk': self.pk})

	def total_likes(self):
		return self.likes.count()

class Comment(models.Model):

	post      = models.ForeignKey(Post, on_delete=models.CASCADE) 
	user      = models.ForeignKey(User, on_delete=models.CASCADE)
	comment   = models.TextField(max_length = 200)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{comment}, {user}'.format(comment = self.comment, user = self.user.username)