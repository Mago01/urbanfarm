from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.farm),
    url(r'^/add$', views.add),
    url(r'^/create$', views.create),
    url(r'^/shop$', views.shop),
    url(r'^/item/(?P<id>\d+)$', views.item),
    url(r'^/update/(?P<id>\d+)$', views.update),
    url(r'^/edit$', views.edit)
    ]
