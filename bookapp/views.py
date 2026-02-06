from django.shortcuts import render
from . models import Books

# Create your views here.
def index(request):
    books=Books.objects.all()
    context={'books':books}
    return render (request, 'index.html', context)