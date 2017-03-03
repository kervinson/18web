from django.contrib.auth.models import User
from django.contrib.auth.models import *
from .forms import UserForm
from django.shortcuts import render,redirect
import uuid
from .models import Verify
from django.core.mail import send_mail

def sign_in(request):

	if request.method == 'GET':
		userinfo = UserForm()
		return render(request,'signin.html',{'userinfo':userinfo})

	else:
		'''
		userinfo = UserForm(request.POST)
		if userinfo.is_valid():
			username = userinfo.clean_data['username']
			password = userinfo.clean_data['password']
			email = userinfo.clean_data['email']
			confpwd = userinfo.clean_data['confpwd']
			user = User.objects.create_user(username=username,password=password,email=email)
			user.is_active = True
			user.save()
			active_code = str(uuid.uuid4().replace('-',''))
			return render('success.html',{'username':username,'active_code':active_code})
		'''
		username = request.POST['username'].strip()
		email = request.POST['email'].strip()
		password = request.POST['password'].strip()
		confpwd = request.POST['confpwd'].strip()
		try:
			user = User.objects.get(email=email)
		except:
			return render(request,'register.html',{'error':'该邮箱已经注册！'})
			
		if not username or not email or not password:
			return render(request,'register.html',{'error':'用户名、邮箱、密码都不能为空','username':username,'email':email})
		if len(username)>20 or len(email) > 20 or len(password) > 20:
			return render(request,'register.html',{'error':'用户名、邮箱、密码都不能太长','username':username,'email':email})
		if password != confpwd:
			return render(request,'register.html',{'error':'密码不一致，请重新输入'})
			
		#user = User(username=username,password=password,email=email,is_active=1,is_staff=1,is_superser=0)
		user = User.objects.create_user(username=username,password=password,email=email)
		user.is_active = False
		user.save()
		active_code = str(uuid.uuid4()).replace('-','')
		verify = Verify(username=username,active_code=active_code)
		verify.save()
		active_link = "http://%s/activate/%s" %(request.get_host(),active_code)
		active_email = '''点击<a href='%s'>这里</a>激活''' %active_link
		send_mail(subject='[Python 部落论坛]激活邮件,',
				message='点击链接激活：%s'%active_link,
				from_email='417933681@qq.com',
				recipient_list=[email],
				fail_silently=False)

		return redirect('/signinsuccess')

def success(request):
	return render(request,'signsuccess.html')

def activate(request,active_code):
	verify = Verify.objects.get(active_code=active_code)
	print ('+++++++')
	username = verify.username
	print (username)
	user=User.objects.get(username=username)
	user.is_active = True
	user.save()
	return render(request,'active.html')