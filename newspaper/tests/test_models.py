from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Article


class ModelTests(TestCase):
    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="Username",
            password="Password",
            first_name="First Name",
            last_name="Last Name",
            years_of_experience=22,
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )
        self.assertEqual(redactor.years_of_experience, 22)
        self.assertTrue(redactor.check_password("Password"))
        self.assertEqual(redactor.username, "Username")
        self.assertEqual(redactor.first_name, "First Name")
        self.assertEqual(redactor.last_name, "Last Name")

    def test_topic_str(self):
        topic = Topic.objects.create(
            name="Topic",
        )
        self.assertEqual(str(topic), topic.name)

    def test_article_str(self):
        article = Article.objects.create(
            title="Title",
            content="Article content",
        )
        self.assertEqual(
            str(article),
            f"{article.title}, {article.date_of_publish}"
        )
