from django.urls import path

from newspaper.views import (
    index,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    TopicListView,
    TopicDetailView,
    TopicCreateView,
    TopicDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path(
        "articles/create/",
        ArticleCreateView.as_view(),
        name="article-create",
    ),
    path(
        "articles/<int:pk>/update/",
        ArticleUpdateView.as_view(),
        name="article-update",
    ),
    path(
        "articles/<int:pk>/delete/",
        ArticleDeleteView.as_view(),
        name="article-delete",
    ),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create",
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create",
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),
]

app_name = "newspaper"
