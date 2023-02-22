from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from django.contrib.auth.models import User


class IndexView(ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'latest_posts'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'index'
        return context

    def get_queryset(self):
        return Post.objects.all().order_by("-pk")


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        post = Post.objects.get(slug=self.kwargs.get('post_slug'))
        context = super().get_context_data(**kwargs)
        context['tags'] = post.tags.all()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/test_add_post.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('index'))

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        initial['title'] = "Its test title"
        return initial.copy()


class AuthorDetailView(DetailView):
    model = User
    template_name = 'main/detail_author.html'
    pk_url_kwarg = 'author_id'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        author = User.objects.get(pk=self.kwargs.get('author_id'))
        context = super().get_context_data(**kwargs)
        context['posts'] = author.post.all()
        return context


class ProfileUserView(DetailView):
    model = User
    template_name = 'main/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile'
