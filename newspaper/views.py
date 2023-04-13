from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import (
    ArticleForm,
    RedactorCreateForm,
    RedactorUpdateForm, ArticleTitleSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = ArticleTitleSearchForm(initial={
            "title": title
        })
        return context

    def get_queryset(self):
        queryset = Article.objects.all()
        title = self.request.GET.get("title")

        if title:
            return queryset.filter(title__icontains=title)

        return queryset


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

    def get_success_url(self):
        return reverse_lazy(
            "newspaper:article-detail",
            kwargs={'pk': self.kwargs['pk']}
        )


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 3


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("articles__topic")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
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


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 6


class TopicDetailView(generic.DetailView):
    model = Topic
    queryset = Topic.objects.all().prefetch_related("articles__publishers")


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")

