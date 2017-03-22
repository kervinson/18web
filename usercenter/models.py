from  django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.IntegerField('性别', choices=((0,u'男'),(1,u'女')), default=0)
    birthday = models.DateTimeField('生日',null=True,blank=True)
    avatar = models.CharField('头像',max_length=300,blank=True)

    def __str__(self):
        return self.avatar

    class Meta:
        verbose_name = '用户档案'
        verbose_name_plural = '用户档案'