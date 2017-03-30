from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^$', views.farm),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^shop$', views.shop),

    ]
