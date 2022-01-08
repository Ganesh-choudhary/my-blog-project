from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request): 
     post = {
          "author": "ganesh choudhary",
          "title": "Test blog post",
          "content": "Thi is text post",
          "published_at": datetime 
     }
     context = {
          "title": "Home Page | Blog Series",
          "posts": [post],
     }
     return render(request, "blog/home.html",context=context)



def about(request):
   return render(request, "blog/about.html")


