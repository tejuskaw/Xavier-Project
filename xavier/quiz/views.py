from django.shortcuts import render,redirect
from .models import Answers , Short_type_question , mcq_type_question
from django.contrib.auth.forms import  AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User


'''
class Write(forms.ModelForm):
    class Meta :
        fields = ['content']'''

def time(user):
    dt=user.answers.login_time
    t=str(dt).split(' ')[1]
    d=str(dt).split(' ')[0]
    minute = int(t.split('.')[0].split(':')[1])+10
    hour= int(t.split('.')[0].split(':')[0])
    if minute >=60 :
        minute = minute -60
        hour = hour +1
    return f"{d.split('-')[1]} {d.split('-')[2]}, {d.split('-')[0]} {str(hour)}:{str(minute)}:{t.split('.')[0].split(':')[2]}"


def evaluate(user):
    sc=0
    ans=User.objects.filter(id=user.id)[0].answers

    if ans.answer1 == mcq_type_question.objects.all()[0].correct_option.lower():
        sc=sc+1
    if ans.answer2 == mcq_type_question.objects.all()[1].correct_option.lower():
        sc=sc+1
    if ans.answer3 == mcq_type_question.objects.all()[2].correct_option.lower():
        sc=sc+1
    if ans.answer4 == mcq_type_question.objects.all()[3].correct_option.lower():
        sc=sc+1
    if ans.answer5 == mcq_type_question.objects.all()[4].correct_option.lower():
        sc=sc+1
    if ans.answer6 == mcq_type_question.objects.all()[5].correct_option.lower():
        sc=sc+1
    if ans.answer7 == mcq_type_question.objects.all()[6].correct_option.lower():
        sc=sc+1
    if ans.answer8 == mcq_type_question.objects.all()[7].correct_option.lower():
        sc=sc+1
    if ans.answer9 == mcq_type_question.objects.all()[8].correct_option.lower():
        sc=sc+1
    if ans.answer10 == mcq_type_question.objects.all()[9].correct_option.lower():
        sc=sc+1

    us = User.objects.filter(id=user.id)[0]
    ans.score = sc
    ans.save()
    return sc





def quiz(request):	
    form = AuthenticationForm()


    if request.user.is_authenticated:

        if request.method == 'POST':
            ans=User.objects.filter(id=request.user.id)[0].answers

            ans.answer1= request.POST.get("a1", "")
            ans.answer2= request.POST.get("a2", "")
            ans.answer3= request.POST.get("a3", "")
            ans.answer4= request.POST.get("a4", "")
            ans.answer5= request.POST.get("a5", "")
            ans.answer6= request.POST.get("a6", "")
            ans.answer7= request.POST.get("a7", "")
            ans.answer8= request.POST.get("a8", "")
            ans.answer9= request.POST.get("a9", "")
            ans.answer10= request.POST.get("a10", "")

            ans.save()
            us=request.user
            logout(request)
            if us.answers.choice == 'short' :
                
                return render(request, 'quiz/quiz.html' , {'submitted' : 'sub' } )
            elif us.answers.choice == 'mcq' :
                score = evaluate(us)
                return render(request, 'quiz/mcq.html' , {'submitted' : 'sub' , 'score' : score} )






        if request.user.answers.choice == 'short' :
            return render(request, 'quiz/quiz.html' , {'time' : time(request.user) , 'quiz' : 'quiz' , 'ques' : Short_type_question.objects.all()}  )
        elif request.user.answers.choice == 'mcq' :
            return render(request, 'quiz/mcq.html' , {'time' : time(request.user) , 'quiz' : 'quiz' , 'ques' : mcq_type_question.objects.all()}  )

    	
    if request.method == 'GET':
        pass

    if request.method == 'POST':

        #login
        if request.POST['action'] == 'login':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)

                    #quiz session starts
                    try:
                        choice=request.POST.get("choice", "")
                        Answers.objects.create(user=request.user , choice=choice )
                    except:
                        use = User.objects.filter(id=request.user.id)[0]
                        logout(request)
                        if use.answers.choice == 'short' :
                            return render(request, 'quiz/quiz.html' , {'submitted' : 'sub'} )
                        elif use.answers.choice == 'mcq' :
                            return render(request, 'quiz/mcq.html' , {'submitted' : 'sub' , 'score' : use.answers.score} )



                    return redirect('quizpage')
                else:
                    form.error_messages['nouser']= _('No such user found')
                    raise forms.ValidationError(
                    form.error_messages['nouser'],
                    code='nouser',)
                    return render(request, 'quiz/login.html' , {'form' : form})
            else:
                # If there were errors, we render the form with these
                # errors
                return render(request, 'quiz/login.html' , {'form' : form}) 
        	    
    return render(request, 'quiz/login.html' , {'form' : form}) 




def about(request):
    return render(request, 'quiz/about.html') 

	

def help(request):
    return render(request, 'quiz/help.html') 
	



def contact(request):
    return render(request, 'quiz/contacts.html') 
	



    