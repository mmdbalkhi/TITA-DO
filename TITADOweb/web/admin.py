from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import TODO, Token

admin.site.register(TODO)
admin.site.register(Token)
