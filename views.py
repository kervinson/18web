'''
from django.http import HttpResponse

def index(request):
	return HttpResponse('Hello world')
'''

from django.shortcuts import render
from block.models import Block

block_info = Block.objects.all().order_by("-id")

def index(request):
    return render(request,'index.html',{'blocks':block_info})