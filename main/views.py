# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def main(request):
    import datetime
    now = datetime.datetime.now()
    """
    'Django 很棒'
    Render the main page
    """
    context = {'like': 'Django 很棒',
               'time': now}
    return render(request, 'main/main.html', context)


def about(request):
    """
    Render the about page
    """
    return render(request, 'main/about.html')

# Create your views here.
