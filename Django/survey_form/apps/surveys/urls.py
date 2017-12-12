from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys$', views.index),
    url(r'^surveys/process$', views.submit, name='submit'),
    url(r'^result$', views.result)
]
