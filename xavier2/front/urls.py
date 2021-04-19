from django.urls import path
from . import views

urlpatterns=[path('',views.main ,  name='mainpage'),
			path('logout/',views.logout_view ,  name='logout'),
			path('discussions/',views.discuss ,  name='discusspage'),
			path('discussions/main/',views.discuss_main ,  name='discussmainpage'),
			path('add/',views.add ,  name='addpage'),
			path('study/',views.study ,  name='studypage'),
			path('quiz/',views.quiz ,  name='quizpage'),
			path('sign/',views.sign ,  name='signpage')
]
