from django.conf.urls import url
from .views import sign_in
from .views import success

urlpatterns = [
	url(r'^signin/',sign_in),
	url(r'^signinsuccess/',success)
]