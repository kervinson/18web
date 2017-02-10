'''
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello world')
'''

from django.shortcuts import render

def index(request):
	return render(request,'index.html')