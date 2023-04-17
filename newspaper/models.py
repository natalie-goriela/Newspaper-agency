from django.db import models
from django.contrib.auth.models import AbstractUser


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_of_publish = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(Topic, related_name="articles")
    publishers = models.ManyToManyField(Redactor, related_name="articles")

    class Meta:
        ordering = ["-date_of_publish"]

    def __str__(self):
        return f"{self.title}, {self.date_of_publish}"
