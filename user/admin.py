from django.contrib import admin
from .models import Verify

class Articleadmin(admin.ModelAdmin):

	list_display = ('username','active_code')

admin.site.register(Verify,Articleadmin)