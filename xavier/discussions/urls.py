from django.urls import path
from . import views

urlpatterns=[path('',views.discuss ,  name='discusspage'),
			path('chat/',views.chat ,  name='chatpage')
]