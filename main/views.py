from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Count

from .models import *


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:4]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'main/index.html', context)


# posts
def detail_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'post': post,
        'tags': post.tags.all()
    }
    return render(request, 'main/detail_post.html', context)


# Author
def detail_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {
        'author': author,
        'posts': author.posts.all()
    }
    return render(request, 'main/detail_author.html', context)


def show_all_authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'main/show_authors.html', context)
