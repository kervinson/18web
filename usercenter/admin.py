from django.contrib import admin
from .models import UserProfile

class Usercenteradmin(admin.ModelAdmin):
    list_display = ('user','sex','birthday')

admin.site.register(UserProfile,Usercenteradmin)