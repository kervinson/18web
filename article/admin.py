from django.contrib import admin
from .models import Article
from comment.admin import Comment

class CommentInline(admin.StackedInline):
    model = Comment
    can_delete = False

class Articleadmin(admin.ModelAdmin):

    list_display = ('title','content','owner','create_timestamp','last_update_timestamp')

    actions = ['make_picked']
    def make_picked(self,request,queryset):
        for a in queryset:
            a.status = 10
            a.save()
    make_picked.short_description = '设置精华'

    readonly_fields = ('owner', 'content', 'status', 'create_timestamp', 'last_update_timestamp')
    inlines = [CommentInline]
    fieldsets = (
        ('基本',{'classes':('wide',),
               'fields':('title','content')}),
        ('高级',{'classes':('collapse',),
               'fields':('status',)}),
    )

admin.site.register(Article,Articleadmin)