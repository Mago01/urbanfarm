from django.conf.urls import include, url
from django.contrib import admin
from apps.shop import views

urlpatterns = [
    url(r'^$', views.index, name= 'shop_index'),
    url(r'^addProduct', views.add, name = 'shop_add'),
    url(r'^cart', views.cart, name = 'shop_cart'),
    url(r'^delete/(?P<cart_id>\d+)/$', views.delete, name='shop_delete'),
    ]