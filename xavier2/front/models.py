from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random , string

from django.conf import settings
from django.contrib.auth import get_user_model




def get_code():
	return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(8))

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Discussion(models.Model):


	title = models.CharField(max_length=30  , default='Please help me with this')
	content = models.TextField()
	time= models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User , on_delete =  models.SET(get_sentinel_user))
	room = models.CharField(max_length=8, default=get_code)

	def __str__(self):
		return f'{self.title} : {self.content}'

	



class Comment(models.Model):
	content = models.TextField()
	time= models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User , on_delete = models.CASCADE)
	room = models.CharField(max_length=8, default='00000000')

	def __str__(self):
		return f'{self.author} : {self.content}'

		

class Material(models.Model):
        name = models.CharField(max_length=30  , default='New material')
        topic = models.TextField()
        file = models.FileField(upload_to = 'materials')
        tag = models.CharField(max_length=7, default=None)





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
	title = models.CharField(max_length=30  , default='New announcement')
	content = models.TextField()
	time= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.title} : {self.content}'
