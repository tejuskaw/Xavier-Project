from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Comment
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.http import HttpResponseRedirect



class SendMessage(forms.ModelForm):
	class Meta :
		model = Comment
		fields = ['content']




def discuss(request):
    return HttpResponse(' <p> Announcements here </p>')

def chat(request):

	if not(request.user.is_authenticated):
		return HttpResponse(' <p> Login first </p>')



	if request.method == 'POST':

			send = SendMessage(request.POST )
			if send.is_valid():
				Comment.objects.create(author=request.user , content=send.cleaned_data['content'])
				return redirect('chatpage')



	comments = Comment.objects.all()






	if request.user.is_authenticated:
		send = SendMessage()
		return render(request, 'front/chat.html', {'comments': comments   , 'send' : send})


    