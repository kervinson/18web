from django.conf.urls import url
from .views import article_list
from .views import article_create
from comment.views import  create_comment
from .views import listing

urlpatterns = [
	url(r'^list/(?P<block_id>\d+)',listing),
	url(r'^create/(?P<block_id>\d+)',article_create),
	url(r'^detail/(?P<article_id>\d+)',create_comment),
]
