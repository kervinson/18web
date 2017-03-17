from django.contrib import admin
from .models import Message

class Messageadmin(admin.ModelAdmin):

	list_display = ('owner','content','link','status')

admin.site.register(Message,Messageadmin)