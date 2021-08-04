from django.urls  import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url('^predict_news/$', views.predict_news, name='predict_news')
]
