from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Redactor, Topic, Article


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "date_of_publish"]
    list_filter = ["date_of_publish"]
    search_fields = ["title"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
