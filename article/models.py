# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pubDateTime']

   
class Comment(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title + '-' + str(self.id)
    
    class Meta:
        ordering = ['pubDateTime']
# Create your models here.
