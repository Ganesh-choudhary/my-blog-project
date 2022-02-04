
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):

     post = {
          "author": "ganesh choudhary",
          "title": "This blog post",
          "content": "This is a Text post",
          "published_at": datetime,
     }

     context = {
          "title" : "Home-paage | Blog series",
          "posts": "[[post]",

     } 
     return render(request, "blog/home.html")

def about(request):
          return render(request, "blog/about.html")


