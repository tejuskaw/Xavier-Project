from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Message
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.http import HttpResponseRedirect



class SendMessage(forms.ModelForm):
	class Meta :
		model = Message
		fields = ['content']




def discuss(request):
    return HttpResponse(' <p> Announcements here </p>')

def chat(request):

	if not(request.user.is_authenticated):
		return HttpResponse(' <p> Login first </p>')



	if request.method == 'POST':

			send = SendMessage(request.POST )
			if send.is_valid():
				Message.objects.create(author=request.user , content=send.cleaned_data['content'])
				return redirect('chatpage')



	messages = Message.objects.all()






	if request.user.is_authenticated:
		send = SendMessage()
		return render(request, 'discussions/chat.html', {'messages': messages   , 'send' : send})


    