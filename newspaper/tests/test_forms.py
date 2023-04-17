from django.test import TestCase

from newspaper.forms import RedactorCreateForm


class FormTests(TestCase):
    def test_redactor_creation_with_fields_is_valid(self):
        form_data = {
            "username": "Username",
            "password1": "Pass123-wrd",
            "password2": "Pass123-wrd",
            "first_name": "First Name",
            "last_name": "Last Name",
            "years_of_experience": 12
        }
        form = RedactorCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_redactor_creation_with_incorrect_years_of_experience(self):
        form_data = {
            "username": "Username",
            "password1": "Pass123-wrd",
            "password2": "Pass123-wrd",
            "first_name": "First Name",
            "last_name": "Last Name",
            "years_of_experience": 100
        }
        form = RedactorCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
