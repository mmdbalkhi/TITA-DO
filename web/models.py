from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField



class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return "{}_token".format(self.user)


class Todos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=255)
    text = models.CharField(max_length=1000, default='')
    date = models.DateTimeField()
    checkBox = BooleanField()
    def __unicode__(self):
        return "{}-{}-{}".format(self.date, self.user, self.todo)

