from django.contrib import admin
from .models import Answers , Short_type_question , mcq_type_question

# Register your models here.
admin.site.register(Answers)
admin.site.register(Short_type_question)
admin.site.register(mcq_type_question)
