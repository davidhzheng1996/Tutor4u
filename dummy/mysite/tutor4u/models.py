from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

import datetime
from django.utils import timezone

# Create your models here.


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="",unique=True)
    password=models.CharField(max_length=200,default="")
    star=models.IntegerField(default=0)
    email=models.EmailField(max_length=200,default="")
    gender=models.CharField(max_length=200,default="")
    biography=models.CharField(max_length=2000,default="")
    major=models.CharField(max_length=200,default="")
    is_active = models.BooleanField(_('active'), default=True)
    currentyear=models.CharField(max_length=200,default="")
    course1=models.CharField(max_length=200,default="")
    course2=models.CharField(max_length=200,default="")
    course3=models.CharField(max_length=200,default="")
    grade1=models.CharField(max_length=200,default="")
    grade2=models.CharField(max_length=200,default="")
    grade3=models.CharField(max_length=200,default="")

    USERNAME_FILED = 'name'

    def __str__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
