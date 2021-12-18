
from django.http import HttpResponse

def home(request):
     return HttpResponse("<h1>welcome my home page</h1>")

def about(request):
   return HttpResponse('<h2>welcome my about pages</h2>')