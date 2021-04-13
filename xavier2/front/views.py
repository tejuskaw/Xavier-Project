from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Comment , Announcement , Profile
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm , UserCreationForm



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class SendComment(forms.ModelForm):
	class Meta :
		model = Comment
		fields = ['content']




def main(request):

	if not(request.user.is_authenticated):
		  return redirect('signpage')


	announcements = Announcement.objects.all()[len(Announcement.objects.all())-20:
					] if len(Announcement.objects.all()) > 21 else Announcement.objects.all()

	announcements2 = []
	print(announcements)

	for i in range(len(announcements)-1 , -1 , -1):
		announcements2.append(announcements[i])

	print(announcements2)



	return render(request, 'front/main.html' , {'announcements' : announcements2})



def sign(request):

    if request.method == 'GET':
        form1 = AuthenticationForm()
        form2 = UserCreationForm()
        return render(request, 'front/sign.html', {'form1' : form1 , 'form2' : form2 })

    if request.method == 'POST':

        if request.POST['action'] == 'login':
        	form1 = AuthenticationForm(request=request, data=request.POST)
        	form2 = UserCreationForm()
        	if form1.is_valid():
        	    username = form1.cleaned_data.get('username')
        	    password = form1.cleaned_data.get('password')
        	    user = authenticate(username=username, password=password)
        	    if user is not None:
        	        login(request, user)
        	        return redirect('mainpage')
        	    else:
        	        form1.error_messages['nouser']= _('No such user found')
        	        raise forms.ValidationError(
        	        form1.error_messages['nouser'],
        	        code='nouser',)
        	        return render(request, 'front/sign.html', {'form1' : form1 , 'form2' : form2 })
        	else:
        	    # If there were errors, we render the form with these
        	    # errors
        	    return render(request, 'front/sign.html', {'form1' : form1 , 'form2' : form2 }) 


        if request.POST['action'] == 'signup':
        	form1 = AuthenticationForm()
        	form2 = UserCreationForm(request.POST)
        	if form2.is_valid():
        	    form2.save()
        	    return redirect('signpage')

        	else:
        	    return render(request, 'front/sign.html', {'form1' : form1 , 'form2' : form2 }) 



  






def chat(request):

	if not(request.user.is_authenticated):
		  return redirect('signpage')



	if request.method == 'POST':

			send = SendComment(request.POST )
			if send.is_valid():
				Comment.objects.create(author=request.user , content=send.cleaned_data['content'])
				return redirect('chatpage')



	comments = Comment.objects.all()






	send = SendComment()
	return render(request, 'front/chat.html', {'comments': comments   , 'send' : send})


    



@login_required
def logout_view(request):
    logout(request)
    return redirect('mainpage')
