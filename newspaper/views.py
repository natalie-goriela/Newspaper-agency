from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import (
    ArticleForm,
    RedactorCreationForm,
    RedactorUpdateForm
)
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


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("newspaper:article-list")


class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    success_url = reverse_lazy("newspaper:article-list")


class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    fields = ["title", "content", "topic", "publishers"]
    success_url = reverse_lazy("newspaper:article-detail")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 3


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("articles__topic")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            "newspaper:redactor-detail",
            kwargs={'pk': self.kwargs['pk']}
        )


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")


