from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from webapp.models import Article

# Create your views here.
def index_view(request):
    articles = Article.objects.order_by("updated_at")
    return render(request, 'index.html',{'articles': articles})

def create_article_view(request):
    if request.method == "GET":
        return render(request, "article_create.html")
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        new_article = Article.objects.create(title=title, content=content, author=author)

        return redirect('article_view', pk=new_article.pk)
def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {"article": article}
    return render(request, "article_view.html", context)