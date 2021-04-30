from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Comment , Announcement , Profile , Discussion , Material , question
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm , UserCreationForm
import random



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
		fields = ['content' , 'room']

class NewDiscussion(forms.ModelForm):
	class Meta :
		model = Discussion
		fields = ['content' ,'title']

class NewAnnouncement(forms.ModelForm):
	class Meta :
		model = Announcement
		fields = ['content' ,'title']

class NewMaterial(forms.ModelForm):
	class Meta :
		model = Material
		fields = ['name' ,'file' ,'tag']




def main(request):

	if not(request.user.is_authenticated):
		  return redirect('signpage')


	announcements = Announcement.objects.all()[len(Announcement.objects.all())-20:
					] if len(Announcement.objects.all()) > 21 else Announcement.objects.all()

	announcements2 = []
	

	for i in range(len(announcements)-1 , -1 , -1):
		announcements2.append(announcements[i])




	return render(request, 'front/main.html' , {'announcements' : announcements2})






def discuss(request):

	if not(request.user.is_authenticated):
		  return redirect('signpage')

	discussion = Discussion.objects.all()[len(Discussion.objects.all())-20:
					] if len(Discussion.objects.all()) > 21 else Discussion.objects.all()

	discussion2 = []
	

	for i in range(len(discussion)-1 , -1 , -1):
		discussion2.append(discussion[i])

	



	return render(request, 'front/disc.html' , {'discussions' : discussion2})





def quiz(request ):
	if not(request.user.is_authenticated):
		return redirect('signpage')

	if request.method == 'POST':

		if request.POST['action']=='start':


			try:
				course=request.POST['course']
			except:
				course = None

			if course == None :
				ques = question.objects.all()
			else :
				ques = question.objects.filter(course=course)



			ques2=[]
			while len(ques2)<5:
				q= random.choice(ques)
				if q not in ques2 :
					ques2.append(q)


			return render(request , 'front/mcq.html' , {'ques' : ques2 })

		if request.POST['action']=='submit':
			ids=[]
			ans=[]
			
			for i in range(5):
				ids.append(request.POST.get(f'a{i+1}').split(':')[0]) 
				try :
					ans.append(request.POST.get(f'a{i+1}').split(':')[-1][-1]) 
				except :
					ans.append('x')



						

			score = 0
			ques=[]
			
			for i in range(len(ids)) :
				q= question.objects.filter(id=ids[i])[0]
				ques.append(q)
				if q.correct == ans[i] :
					score+=1
				
					
		
			return render(request , 'front/quizend.html' , {'score' : score , 'ques' : ques , 'ans' : ans})




				
			





	return render(request , 'front/quizstart.html')










def study(request) :
	if not(request.user.is_authenticated):
		return redirect('signpage')




	try:
		tag=request.GET['tag']
	except:
		tag = None

	if tag == None :
		study = Material.objects.all()
	else :
		study = Material.objects.filter(tag=tag)
	

	study2 = []
	

	for i in range(len(study)-1 , -1 , -1):
		study2.append(study[i])

	
	empty = True if len(study2)==0 else False




	return render(request , 'front/study.html' ,  { 'study' : study2 , 'empty' :empty })



def add(request) :
	if not(request.user.is_authenticated):
		return redirect('signpage')


	if request.method == 'POST':

		
		
		if request.POST['action']=='announce':
			send = NewAnnouncement(request.POST)
			if send.is_valid() :
				
				if request.user.is_staff :
					Announcement.objects.create(
				 						content=send.cleaned_data['content'] ,
				 						title=send.cleaned_data['title'])
				print('Announcement')
				
		if request.POST['action']=='discuss':
			send = NewDiscussion(request.POST)
			if send.is_valid() :
				print(request.POST)
				
			
				Discussion.objects.create(author=request.user ,
				 						content=send.cleaned_data['content'] ,
				 						title=send.cleaned_data['title'])

		if request.POST['action']=='study':
			form = NewMaterial(request.POST , request.FILES)
			if form.is_valid() :
				form.save()


			
	send = NewDiscussion()
	send2= NewMaterial()





	return render(request , 'front/add.html' , {'send' : send , 'send2' : send2 })
















def discuss_main(request) :
	if not(request.user.is_authenticated):
		return redirect('signpage')



	if request.method == 'POST':

		send = SendComment(request.POST )
		
		if send.is_valid():
			
			Comment.objects.create(author=request.user ,
			 						content=send.cleaned_data['content'] ,
			 						room=send.cleaned_data['room'])
			
			print('commented ')


	try:
		discuss=request.GET['discuss']
	except:
		return HttpResponse('<h1>No such discussion</h1>')

	discussion = Discussion.objects.filter(room=discuss)[0]
	comments = Comment.objects.filter(room=discussion.room)
	
	comments2 = []
	

	for i in range(len(comments)-1 , -1 , -1):
		comments2.append(comments[i])


	send = SendComment()

	return render(request, 'front/disc_main.html' , {'discussion' : discussion , 'comments' :comments2 , 'send' : send })








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
        	    
        	    return render(request, 'front/sign.html', {'form1' : form1 , 'form2' : form2 }) 


        if request.POST['action'] == 'signup':
        	form1 = AuthenticationForm()
        	form2 = UserCreationForm(request.POST)
        	if form2.is_valid():
        	    form2.save()
        	    return redirect('signpage')

        	else:
        	    return render(request, 'front/sign.html', {'form1' : form1 , 'form2' : form2 }) 



  

    



@login_required
def logout_view(request):
    logout(request)
    return redirect('mainpage')
