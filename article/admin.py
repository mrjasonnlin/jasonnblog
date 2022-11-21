# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Article, Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['article', 'content']
    list_display_links = ['article']
    list_filter = ['article', 'content']
    search_fields = ['content']
    list_editable = ['content']

    class Meta:
        model = Comment


admin.site.register(Article)
admin.site.register(Comment, CommentModelAdmin)
# Register your models here.
