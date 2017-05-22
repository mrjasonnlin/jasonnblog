from django.conf.urls import url
from article import views


urlpatterns = [
    url(r'^$', views.article, name='article'),
    url(r'^articleCreate/$', views.articleCreate, name='articleCreate'),
    url(r'^articleRead/(?P<articleId>[0-9]+)/$', views.articleRead, name='articleRead'),
    url(r'^articleUpdate/(?P<articleId>[0-9]+)/$', views.articleUpdate, name='articleUpdate'),
    url(r'^articleDelete/(?P<articleId>[0-9]+)/$', views.articleDelete, name='articleDelete'),
    url(r'^articleSearch/$', views.articleSearch, name='articleSearch'),
 
]