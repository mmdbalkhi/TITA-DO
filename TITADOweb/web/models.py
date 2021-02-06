# Create your models here.
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # TODO: do not save password

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return "{}_token".format(self.user)

class TODO(models.Model):
    TODO = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.TODO

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __unicode__(self):
        return "{}-{}".format(self.pub_date, self.TODO)


class Choice(models.Model):
    TODO = models.ForeignKey(TODO, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
