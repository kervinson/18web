from django.shortcuts import render,redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
import os
import time

@login_required
def upload_avatar(request):
    if request.method == "GET":
        return render(request,'uploadavatar.html')
    else:
        user = request.user
        profile = UserProfile.objects.get(user=user)
        avatar_file = request.FILES.get('avatar',None)
        if avatar_file.size > 2000:
            return render(request,'uploadavatar.html',{'error':'图片太大，请压缩图片'})
        else:
            avatar_file_name = str(time.time()) + avatar_file.name
            print(avatar_file_name)
            file_path = os.path.join('C:/fu/logistic01/avatar/',avatar_file_name)
            with open(file_path,'wb+') as destination:
                for chunk in avatar_file.chunks():
                    destination.write(chunk)
            url = "http://res.myforum.com/avatar/%s" %avatar_file_name
            profile.avatar = url
            profile.save()
            return redirect("/")

