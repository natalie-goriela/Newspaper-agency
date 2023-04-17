from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Redactor, Article

TOPIC_CREATE_URL = reverse("newspaper:topic-create")
ARTICLE_LIST_URL = reverse("newspaper:article-list")
REDACTOR_LIST_URL = reverse("newspaper:redactor-list")


class PublicTopicCreateTest(TestCase):
    def test_login_required(self):
        response = self.client.get(TOPIC_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            password="Password",
        )
        self.client.force_login(self.user)

    def test_create_redactor(self):
        form_data = {
            "username": "Username",
            "password1": "Pass123-wrd",
            "password2": "Pass123-wrd",
            "first_name": "First Name",
            "last_name": "Last Name",
            "years_of_experience": 12
        }
        self.client.post(
            reverse("newspaper:redactor-create"),
            data=form_data
        )
        created_user = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(created_user.first_name, form_data["first_name"])
        self.assertEqual(created_user.last_name, form_data["last_name"])
        self.assertEqual(
            created_user.years_of_experience,
            form_data["years_of_experience"]
        )


class PublicRedactorListTests(TestCase):
    def setUp(self) -> None:
        Redactor.objects.create(
            username="Test1",
            first_name="Test1",
            last_name="Driver",
            years_of_experience=22
        )

        Redactor.objects.create(
            username="Test2",
            first_name="Test2",
            last_name="Driver",
            years_of_experience=2
        )

        Redactor.objects.create(
            username="Test3",
            first_name="Test3",
            last_name="Driver",
            years_of_experience=8
        )

        Redactor.objects.create(
            username="Test45",
            first_name="Test4",
            last_name="Driver",
            years_of_experience=5
        )

    def test_redactor_list_pagination_is_three(self):
        response = self.client.get(REDACTOR_LIST_URL)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["redactor_list"]), 3)

    def test_lists_all_redactors(self):
        response = self.client.get(REDACTOR_LIST_URL + "?page=2")
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["redactor_list"]), 1)


class PublicArticleListTest(TestCase):
    def setUp(self) -> None:
        Article.objects.create(
            title="Test",
            content="Test content"
        )
        Article.objects.create(
            title="Test2",
            content="Test content2"
        )
        Article.objects.create(
            title="Test3",
            content="Test content3"
        )
        Article.objects.create(
            title="Test4",
            content="Test content4"
        )

    def test_retrieve_article_list(self):

        response = self.client.get(ARTICLE_LIST_URL)
        articles = Article.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["article_list"]),
            list(articles)
        )
        self.assertTemplateUsed(
            response,
            "newspaper/article_list.html"
        )

    def test_article_list_pagination_is_four(self):
        Article.objects.create(
            title="Test5",
            content="Test content5"
        )
        response = self.client.get(ARTICLE_LIST_URL)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["article_list"]), 4)

    def test_lists_all_articles(self):
        Article.objects.create(
            title="Test5",
            content="Test content5"
        )
        response = self.client.get(ARTICLE_LIST_URL + "?page=2")
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["article_list"]), 1)

    def test_article_filter_by_title_is_valid(self):
        article1 = Article.objects.create(
            title="New Test5",
            content="Test content5"
        )

        response = self.client.get(ARTICLE_LIST_URL + "?title=new")
        self.assertEqual(
            list(response.context["article_list"]),
            [article1]
        )
