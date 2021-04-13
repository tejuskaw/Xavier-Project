from django.contrib import admin
from .models import Comment, Profile , Announcement

admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Announcement)

