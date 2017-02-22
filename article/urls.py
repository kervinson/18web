from django.conf.urls import url
from .views import article_list
from .views import article_create
from .views import  article_detail
from .views import listing

urlpatterns = [
	url(r'^list/(?P<block_id>\d+)',article_list),
	url(r'^create/(?P<block_id>\d+)',article_create),
	url(r'^detail/(?P<article_id>\d+)',article_detail),
	url(r'^detail/(?P<article_id>\d+?d+)',listing),
]
