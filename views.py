'''
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')
'''

from django.shortcuts import render,redirect
from block.models import Block
from django.contrib.auth.models import User
from message.models import Message

block_info = Block.objects.filter(status=0).order_by("-id")

def index(request):
    owner = request.user
    msg_cnt = Message.objects.filter(owner=owner,status=0).count()
    print(msg_cnt)
    return render(request,'index.html',{'blocks':block_info,'msg_cnt':msg_cnt})
    #return render(request, 'index.html', {'blocks': block_info})


def register(request):

    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        confpwd = request.POST['confpwd'].strip()

        if not username or not email or not password:
            return render(request,'register.html',{'error':'用户名、邮箱、密码都不能为空','username':username,'email':email})
        if len(username)>20 or len(email) > 20 or len(password) > 20:
            return render(request,'register.html',{'error':'用户名、邮箱、密码都不能太长','username':username,'email':email})
        if password != confpwd:
            return render(request,'register.html',{'error':'密码不一致，请重新输入'})
        #user = User(username=username,password=password,email=email,is_active=1,is_staff=1,is_superser=0)
        user = User.objects.create_user(username=username,password=password,email=email)
        user.is_active = True
        user.save()
        return redirect('/admin')