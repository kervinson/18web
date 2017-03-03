from django.db import models

class Verify(models.Model):
	username = models.CharField('用户名',max_length=20)
	active_code = models.CharField('验证码',max_length=40)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name='用户验证'
		verbose_name_plural = '用户验证'