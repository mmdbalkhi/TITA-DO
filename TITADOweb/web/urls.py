from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/TODO/$', views.submit_TODO, name='TODO')
]
