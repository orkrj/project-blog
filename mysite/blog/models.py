from dataclasses import field

from django.utils import timezone

from django.db import models


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    statue = models.CharField(
        max_length=2, # DF or PB
        choices=Status.choices,
        default=Status.DRAFT,
    )

    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published']),
        ]

    def __str__(self):
        return self.title