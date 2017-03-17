from django.conf.urls import url

from .views import message_list,read_message

urlpatterns = [
	url(r'^list/',message_list),
    url(r'^read/(?P<msg_id>\d+)',read_message),
]