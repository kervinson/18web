from django.conf.urls import url
from .views import post_detail,post_list,post_share

urlpatterns = [
    #post views
    url(r'^$',post_list,name='post_list'),
    #url(r"^$",PostListView.as_view(),name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        post_detail,
        name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$',post_share,name='post_share'),
]