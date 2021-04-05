from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def material(request):
    return HttpResponse(' <p> material here </p>')
