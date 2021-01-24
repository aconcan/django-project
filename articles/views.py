from django.shortcuts import render
# from models in the current folder
from .models import Article

def article_list(request):
    # Retrieving all Article objects from DB
    articles = Article.objects.all().order_by('date')
    # Passing articles dictonary to the template. to render the data
    return render(request, 'articles/article_list.html', {'articles': articles})