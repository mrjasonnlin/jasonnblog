# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    fullName = models.CharField(max_length=128)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'

# Create your models here.
