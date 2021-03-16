from django.urls import path
from . import views

urlpatterns=[path('',views.quiz ,  name='quizpage'),
			path('about/',views.about ,  name='aboutpage'),
			path('help/',views.help ,  name='helppage'),
			path('contact/',views.contact ,  name='contactpage')
]