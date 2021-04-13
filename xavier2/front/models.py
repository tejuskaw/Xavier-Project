from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Comment(models.Model):
	content = models.TextField()
	time= models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User , on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.author} : {self.content}'






class Profile(models.Model):
	user= models.OneToOneField(User , on_delete = models.CASCADE )
	image = models.ImageField(default='default.jpg' , upload_to = 'profile_pics')
	bg = models.ImageField(default= 'default.jpg'  , upload_to = 'bg_pics')
	color = models.CharField(max_length=7, default='#000000')


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img=Image.open(self.image.path)

		if img.height >300 or img.width > 300 :
			img.thumbnail((300,300))
			img.save(self.image.path)




class Announcement(models.Model):
	content = models.TextField()
	time= models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User , on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.author} : {self.content}'