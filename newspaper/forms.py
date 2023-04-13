from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator

from newspaper.models import Article, Topic, Redactor


class ArticleForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    topic = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Article
        fields = ["title", "content", "topic", "publishers"]


class RedactorCreateForm(UserCreationForm):
    MAX_EXPERIENCE_VALUE = 55

    years_of_experience = forms.IntegerField(
        required=True,
        validators=[MaxValueValidator(MAX_EXPERIENCE_VALUE)]
    )

    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = ("first_name", "last_name", "email")


class ArticleTitleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."}),
    )
