from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Div,
    Submit,
    HTML,
    Row,
    Column,
    Field,
    Fieldset,
    MultiField,
)
from security.models import User, Profile


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Column(
                    Fieldset("Register Form", css_class="text-muted text-center h6")
                ),
                css_class="border-bottom",
            ),
            Column(
                Field("username", css_class="col-md-12"),
                Field("email", css_class="col-md-12"),
            ),
            Row(
                Field("first_name", css_class="col-md-6"),
                Field("last_name", css_class="col-md-6"),
            ),
            Column(
                Field("password1", css_class="col-md-12"),
                Field("password2", css_class="col-md-12"),
            ),
            Submit("submit", "create user", css_class="btn btn-primary w-100"),
        )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        )
    )

    class Meta:
        model = Profile
        fields = [
            "photo",
            "email",
            "first_name",
            "last_name",
            "postal_code",
            "country",
            "state",
            "address",
            "phone_number",
            "phone_number2",
            "birth_date",
            "bio",
            "about_blog",
        ]

    def save(self, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.save()
        return profile
