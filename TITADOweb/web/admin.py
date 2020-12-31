from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Todos, Token

admin.site.register(Todos)
admin.site.register(Token)
