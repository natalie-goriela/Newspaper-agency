from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import ArticleForm
from newspaper.models import Redactor, Topic, Article


def index(request):
    """View function for the home page of the site."""

    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_articles = Article.objects.count()

    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_articles": num_articles,
    }

    return render(request, "newspaper/index.html", context=context)


class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 4


class ArticleDetailView(generic.DetailView):
    model = Article


class ArticleCreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("newspaper:article-list")


class ArticleDeleteView(generic.DeleteView):
    model = Article
    success_url = reverse_lazy("newspaper:article-list")


class ArticleUpdateView(generic.UpdateView):
    model = Article
    fields = ["title", "content", "topic", "publishers"]
    success_url = reverse_lazy("newspaper:article-list")

