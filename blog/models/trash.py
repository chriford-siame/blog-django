import uuid
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.timestamp import Timestamp


class Trash(Timestamp):
    post = models.ForeignKey(
        verbose_name=_("Post"),
        to='blog.Post',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    
    def __str__(self):
        return f"{self.post.title} - trash-{self.pk}"
