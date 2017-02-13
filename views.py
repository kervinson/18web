'''
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello world')
'''

from django.shortcuts import render

blocks_info = [
    {'name':'运维专区','manager':'admin','desc':'运维人员看过来'},
    {'name':'django专区','manager':'admin','desc':'django学习讨论专区'},
    {'name':'部落建设','manager':'admin','desc':'有关部落建设事宜'}
]

def index(request):
    return render(request,'index.html')