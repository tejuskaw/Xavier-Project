from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Answers(models.Model):
	user= models.OneToOneField(User , on_delete = models.CASCADE )

	choice = models.CharField(max_length=5 , default='short' )

	login_time= models.DateTimeField(auto_now_add=True)

	answer1 = models.TextField(default='' )
	answer2 = models.TextField(default='' )
	answer3 = models.TextField(default='' )
	answer4 = models.TextField(default='' )
	answer5 = models.TextField(default='' )
	answer6 = models.TextField(default='' )
	answer7 = models.TextField(default='' )
	answer8 = models.TextField(default='' )
	answer9 = models.TextField(default='' )
	answer10 = models.TextField(default='' )

	score = models.IntegerField(default=0)




	def __str__(self):
		return f'Answers by {self.user.username}'

class Short_type_question(models.Model):

	question = models.TextField()
	image = models.ImageField(default='default.jpg' , upload_to = 'source')

	def __str__(self):
		i=0
		for index, item in enumerate(Short_type_question.objects.all()):
			if item.id==self.id:
				i = index + 1
				break
		return f'{i} : {self.question}' 

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img=Image.open(self.image.path)

		if img.height >200 or img.width > 200 :
			img.thumbnail((200,200))
			img.save(self.image.path)


class mcq_type_question(models.Model):

	question = models.TextField()
	image = models.ImageField(default='default.jpg' , upload_to = 'source')


	option_a = models.CharField(max_length=50)
	option_b = models.CharField(max_length=50)
	option_c = models.CharField(max_length=50)
	option_d = models.CharField(max_length=50)

	correct_option = models.CharField(max_length=1)

	def __str__(self):
		i=0
		for index, item in enumerate(mcq_type_question.objects.all()):
			if item.id==self.id:
				i = index + 1
				break
		return f'{i} : {self.question}' 

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img=Image.open(self.image.path)

		if img.height >200 or img.width > 200 :
			img.thumbnail((200,200))
			img.save(self.image.path)





