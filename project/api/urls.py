from django.conf.urls import url
from django.urls import path
from api import views


urlpatterns = [
	url(r'^persona/list$', views.get_personas, name='get_personas'),
]
