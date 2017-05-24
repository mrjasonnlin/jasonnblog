# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.query_utils import Q
from article.models import Article, Comment
from article.forms import ArticleForm

def article(request):
    '''
    Render the article page
    '''
    articles = Article.objects.all()
    itemList = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemList.append(items)
    context = {'itemList':itemList}
    return render(request, 'article/article.html', context)

def articleCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation; display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        print(ArticleForm())
        return render(request, template, {'articleForm':ArticleForm()})
    # POST
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request, '文章已新增')
    return redirect('article:article')
def articleRead(request, articleId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with the article instance and its
           associated comments
    '''
    article = get_object_or_404(Article, id=articleId)
    context = {
        'article': article,
        'comments': Comment.objects.filter(article=article)
    }
    return render(request, 'article/articleRead.html', context)
def articleUpdate(request, articleId):
    '''
    Update the article instance:
        1. Get the article to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
           bound form with error messages
    '''
    article = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=article)
        return render(request, template, {'articleForm':articleForm, 'article':article})
    # POST
    articleForm = ArticleForm(request.POST, instance=article)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm, 'article':article})
    articleForm.save()
    messages.success(request, '文章已修改') 
    return redirect('article:articleRead', articleId=articleId)
def articleDelete(request, articleId):
    '''
    Delete the article instance:
        1. Render the article page if the method is GET
        2. Get the article to delete; redirect to 404 if not found
    '''
    if request.method == 'GET':
        return article(request)
    # POST
    articleToDelete = get_object_or_404(Article, id=articleId)
    articleToDelete.delete()
    messages.success(request, '文章已刪除')  
    return redirect('article:article')
def articleSearch(request):
    '''
    Search for articles:
        1. Get the "searchTerm" from the HTML page
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    articles = Article.objects.filter(Q(title__icontains=searchTerm) |
                                      Q(content__icontains=searchTerm))
    context = {'articles':articles, 'searchTerm':searchTerm} 
    return render(request, 'article/articleSearch.html', context)
def articleLike(request, articleId):
    '''
    Add the user to the 'likes' field:
        1. Get the article; redirect to 404 if not found
        2. If the user does not exist in the "likes" field, add him/her
        3. Finally, call articleRead() function to render the article
    '''
    article = get_object_or_404(Article, id=articleId)
    if not request.user.article_set.exists():
        article.likes.add(request.user)
    return articleRead(request, articleId)
def commentCreate(request, articleId):
    '''
    Create a comment for an article:
        1. Get the "comment" from the HTML form
        2. Store it to database
    '''
    if request.method == 'GET':
        return articleRead(request, articleId)
    # POST
    comment = request.POST.get('comment')
    if comment:
        comment = comment.strip()
    if not comment:
        return redirect('article:articleRead', articleId=articleId)
    article = get_object_or_404(Article, id=articleId)
    Comment.objects.create(article=article, user=request.user, content=comment)
    return redirect('article:articleRead', articleId=articleId)
def commentUpdate(request, commentId):
    '''
    Update a comment:
        1. Get the comment to update and its article; redirect to 404 if not found
        2. If comment is empty, delete the comment
        3. Else update the comment
    '''
    commentToUpdate = get_object_or_404(Comment, id=commentId)
    article = get_object_or_404(Article, id=commentToUpdate.article.id)
    if request.method == 'GET':
        return articleRead(request, article.id)
    # POST    
    comment = request.POST.get('comment', '').strip()
    if not comment:
        commentToUpdate.delete()
    else:
        commentToUpdate.content = comment
        commentToUpdate.save()
    return redirect('article:articleRead', articleId=article.id)
def commentDelete(request, commentId):
    '''
    Delete a comment:
        1. Get the comment to update and its article; redirect to 404 if not found
        2. Delete the comment
    '''
    comment = get_object_or_404(Comment, id=commentId)
    article = get_object_or_404(Article, id=comment.article.id)
    if request.method == 'GET':
        return articleRead(request, article.id)
    # POST
    comment.delete()
    return redirect('article:articleRead', articleId=article.id)

# Create your views here.
