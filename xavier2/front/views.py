from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Comment
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm



class SendMessage(forms.ModelForm):
	class Meta :
		model = Comment
		fields = ['content']




def discuss(request):

	if not(request.user.is_authenticated):
		  return redirect('signpage')



	return HttpResponse(' <p> Announcements here </p>')



def sign(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'front/sign.html', {'form' : form })

    if request.method == 'POST':

        if request.POST['action'] == 'login':
        	form = AuthenticationForm(request=request, data=request.POST)
        	if form.is_valid():
        	    username = form.cleaned_data.get('username')
        	    password = form.cleaned_data.get('password')
        	    user = authenticate(username=username, password=password)
        	    if user is not None:
        	        login(request, user)
        	        return redirect('chatpage')
        	    else:
        	        form.error_messages['nouser']= _('No such user found')
        	        raise forms.ValidationError(
        	        form.error_messages['nouser'],
        	        code='nouser',)
        	        return render(request, 'front/sign.html', { 'form': form })
        	else:
        	    # If there were errors, we render the form with these
        	    # errors
        	    return render(request, 'front/sign.html', { 'form': form }) 


  






def chat(request):

	if not(request.user.is_authenticated):
		  return redirect('signpage')



	if request.method == 'POST':

			send = SendMessage(request.POST )
			if send.is_valid():
				Comment.objects.create(author=request.user , content=send.cleaned_data['content'])
				return redirect('chatpage')



	comments = Comment.objects.all()






	send = SendMessage()
	return render(request, 'front/chat.html', {'comments': comments   , 'send' : send})


    