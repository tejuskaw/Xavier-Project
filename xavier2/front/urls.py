from django.urls import path
from . import views

urlpatterns=[path('',views.main ,  name='mainpage'),
			path('chat/',views.chat ,  name='chatpage'),
			path('logout/',views.logout_view ,  name='logout'),
			path('discussions/',views.discuss ,  name='discusspage'),
			path('discussions/main/',views.discuss_main ,  name='discussmainpage'),
			path('sign/',views.sign ,  name='signpage')
]