from django.shortcuts import render
from .models import Article


def show_articles(request):
    return render(
        request,
        'articles.html',
        context={"articles": Article.objects.all()}

    )


def show_article(request, id):
    return render(
        request,
        'article.html',
        context={"article": Article.objects.get(id=id)}
    )
