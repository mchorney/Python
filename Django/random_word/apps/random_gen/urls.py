from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.index),
    url(r'^generate$', views.generate, name='generate'),
    url(r'^random_word/reset$', views.reset, name='reset')
]
