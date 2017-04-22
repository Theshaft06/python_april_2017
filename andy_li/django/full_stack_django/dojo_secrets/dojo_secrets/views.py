# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

def current_user(request):
    return User.objects.get(id = request.session["user_id"])


def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "dojo_secrets/index.html")

def createUser(request):
    print "-= Reached /users (redirect to secrets.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate user reg fields
    check = User.objects.validateUserReg(request.POST)
    if check["pass"] is False:
        for error in check["errors"]:
            messages.error(request, error)
        return redirect("/")

    # create user
    hashed_pwd = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
    user = User.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        email = request.POST["email"],
        password = hashed_pwd,
    )
    print User.objects.all()
    # created user into db, add user id to session to log in
    request.session["user_id"] = user.id
    print request.session.items()
    return redirect("/secrets")


def login(request):
    print "-= Reached /login (redirect to secrets.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate login via validateUserLog from models.py
    check = User.objects.validateUserLog(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
        return redirect("/")

    # valid email, password for login, store user id to session, go to secrets.html
    request.session["user_id"] = check["user"].id
    print request.session.items()
    return redirect("/secrets")


def secrets(request):
    print "-= Reached /secrets (secrets.html) =-"
    # if request.method != "POST":
    #     return redirect("/")
    data = {
        "current_user": current_user(request),
        "posts": Post.objects.all(),
    }

    return render(request, "dojo_secrets/secrets.html", data)


def logout(request):
    print "-= Reached /logout (redirect to /) =-"
    request.session.clear()
    return redirect("/")


def createPost(request):
    print "-= Reached /posts (redirect to secrets.html) =-"
    if request.method != "POST":
        return redirect("/")

    check = Post.objects.validatePost(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
    else:
        post = Post.objects.create(
            post = request.POST["post"],
            user = current_user(request),
        )
    return redirect("/secrets")
