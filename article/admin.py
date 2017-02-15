from django.contrib import admin
from .models import Article

class Articleadmin(admin.ModelAdmin):

	list_display = ('title',.'content','create_timestamp','last_update_timestamp')

admin.site.register(Article,Articleadmin)