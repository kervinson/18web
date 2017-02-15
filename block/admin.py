#coding=utf-8
from django.contrib import admin

from .models import Block


class Blockadmin(admin.ModelAdmin):
	list_display = ('name','desc','manager')

admin.site.register(Block,Blockadmin)