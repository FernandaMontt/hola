# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


def index(request):
			posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
			return render(request, 'blog/index.html', {'posts': posts})
			
