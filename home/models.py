# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Person(models.Model):

    #__Person_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    birth = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Person_FIELDS__END

    class Meta:
        verbose_name        = _("Person")
        verbose_name_plural = _("Person")


class Address(models.Model):

    #__Address_FIELDS__
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    #__Address_FIELDS__END

    class Meta:
        verbose_name        = _("Address")
        verbose_name_plural = _("Address")



#__MODELS__END
