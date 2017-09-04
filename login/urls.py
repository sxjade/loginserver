from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lg', views.login, name='login'),
    url(r'^in', views.insetuser, name='insetuser'),
]