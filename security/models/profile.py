from django.db import models
from django.utils.translation import gettext_lazy as _
from security.manager import CustomUserManager

from blog.models import Timestamp


class Profile(Timestamp):
    user_id = models.CharField(
        verbose_name=_("User ID"),
        max_length=255,
        null=True,
        blank=True,
        editable=False,
    )
    photo = models.ImageField(
        verbose_name=_("Photo"),
        upload_to="profile/photo/%H-%M-%S-%y",
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=255,
        null=True,
        blank=False,
    )
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=255,
        null=True,
        blank=False,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=255,
        null=True,
        blank=False,
    )
    country = models.CharField(
        verbose_name=_("Country"),
        max_length=25,
        null=True,
        blank=True,
    )
    state = models.CharField(
        verbose_name=_("State/Province"),
        max_length=15,
        null=True,
        blank=True,
    )
    postal_code = models.CharField(
        verbose_name=_("Postal code"),
        max_length=10,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name=_("Phone number"),
        default="+260",
        max_length=255,
        null=True,
        blank=False,
    )
    phone_number2 = models.CharField(
        verbose_name=_("Phone number 2"),
        default="+260",
        max_length=255,
        null=True,
        blank=True,
    )
    address = models.CharField(
        verbose_name=_("Address"),
        max_length=255,
        null=True,
        blank=True,
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
    )
    bio = models.TextField(
        verbose_name=_("Bio"),
        max_length=1000,
        null=True,
        blank=True,
    )
    about_blog = models.TextField(
        verbose_name=_("About Blog"),
        null=True,
        blank=True,
    )
    def __str__(self):
        return f"Profie | {self.first_name} {self.last_name} | User ID - {self.user_id}"

    @property
    def form(self):
        from security.forms import UserProfileForm

        return UserProfileForm(instance=self)
