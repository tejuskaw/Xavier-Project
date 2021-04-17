from django.contrib import admin
from .models import Comment, Profile , Announcement , Discussion , Material

admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Announcement)
admin.site.register(Discussion)
admin.site.register(Material)
