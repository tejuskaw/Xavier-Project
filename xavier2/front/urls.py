from django.urls import path
from . import views

urlpatterns=[path('',views.main ,  name='mainpage'),
			path('chat/',views.chat ,  name='chatpage'),
			path('logout/',views.logout_view ,  name='logout'),
			path('discussions/',views.discuss ,  name='discusspage'),
			path('sign/',views.sign ,  name='signpage')
]