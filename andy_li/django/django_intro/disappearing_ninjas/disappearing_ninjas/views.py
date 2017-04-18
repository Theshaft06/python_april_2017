# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "disappearing_ninjas/index.html")

def ninjas(request, color):
    print "-= Reached /ninjas/<color> =-"
    if color == "":
        img = "tmnt_all"
    elif color == "blue":
        img = "leo"
    elif color == "orange":
        img = "mikey"
    elif color == "red":
        img = "raph"
    elif color == "purple":
        img = "don"
    else:
        img = "april"

    data = {
        "img": img
    }
    print data
    return render(request, "disappearing_ninjas/ninjas.html", data)
