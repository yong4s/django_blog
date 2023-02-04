from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
from django.contrib.auth import authenticate

from .models import *
from .forms import *
from django.contrib.auth.models import User


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-pk")[:4]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'main/in-dex.html', context)


# posts
def detail_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'post': post,
        'tags': post.tags.all()
    }
    return render(request, 'main/detail_post.html', context)


@require_GET
def show_form(request):
    if request.user.is_authenticated:
        form = AddPostForm()
        return render(request, 'main/add_post.html', {'form': form})
    else:
        messages.info(request, 'Для публікації потрібно увійти у свій аккаунт')
        return HttpResponseRedirect(reverse('login'))


@require_POST
def add_post(request):
    form = AddPostForm(request.POST or None, request.FILES or None)
    if not form.is_valid():
        return HttpResponseRedirect(reverse('show_form'))

    article = form.save(commit=False)
    article.user = request.user
    article.save()
    messages.success(request, 'Success')
    return HttpResponseRedirect(reverse('index'))


def detail_author(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    context = {
        'author': author,
        'posts': author.post.all()
    }
    return render(request, 'main/detail_author.html', context)