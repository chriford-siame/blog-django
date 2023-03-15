import uuid
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.timestamp import Timestamp

class Image(Timestamp):
    file = models.ImageField(
        upload_to='%D-%M-%Y/blog-images',
        null=True,
        blank=False,
    )
    post = models.ForeignKey(
        to='blog.Post',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    
    def __str__(self):
        return f"{self.post.title} - image-{self.pk}"