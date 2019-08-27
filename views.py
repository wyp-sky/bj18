from django.http import Httpresponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse('index')

def login(requets):
    return redirect('/index')

