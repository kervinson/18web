from django.contrib import admin
from .models import Comment

class Commentadmin(admin.ModelAdmin):

	list_display = ('article','owner','content','status','create_timestamp','last_update_timestamp')

admin.site.register(Comment,Commentadmin)