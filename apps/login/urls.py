from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$',views.register),
    url(r'^logout$',views.logout),
    url(r'^home$',views.home),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
