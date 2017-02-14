#coding=utf-8
from django.db import models

class Block(models.Model):

	name = models.CharField(u'板块名称',max_length=100)
	desc = models.CharField(u'板块描述',max_length=100)
	manager = models.CharField(u'管理员名称',max_length=100)