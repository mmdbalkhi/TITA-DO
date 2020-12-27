from django.conf.urls import url
from django.urls import path

from .views import Todo 


urlpatterns = [
    url(r'^submitTodo/$', Todo, name='Todo'),
]
