from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from .forms import *


def register_user(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()

            login(request, new_user)
            messages.info(request, "Registration successful")

            return HttpResponseRedirect(reverse("index"))
    else:
        form = RegisterForm()

    context["form"] = form

    return render(request, "user/register.html", context)


def login_user(request):
    context = {}

    if request.user.is_authenticated:
        messages.info(request, 'You are authenticated')
        return HttpResponseRedirect(reverse('index'))

    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Success')
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, "Invalid data")
    else:
        form = LoginForm()

    context['form'] = form
    return render(request, 'user/login.html', context)


