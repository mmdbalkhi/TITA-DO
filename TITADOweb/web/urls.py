from django.conf.urls import url
from django.urls import path

from .views import Todo

urlpatterns = [
    #url(r'^submitTodo/$', submitTodo, name='submitTodo'),
    path('submitTodo/', Todo, name='Todo')
]
