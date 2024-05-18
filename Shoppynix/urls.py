
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
#name of ulrs.-:
    #path("",include("blog.urls")),
    path("",include("blog.urls")),
]
