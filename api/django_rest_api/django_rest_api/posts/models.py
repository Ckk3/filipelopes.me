from django.db import models


class Post(models.Model):
    class TypeOfContent(models.TextChoices):
        IMAGE = 'IMG'
        VIDEO = 'VID'
        TEXT = 'TXT'
        HTML = 'HTML'

    title_pt_br = models.CharField(max_length=200, blank=True)
    title_en_us = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    excerpt_pt_br = models.TextField(blank=True)
    excerpt_en_us = models.TextField(blank=True)
    content_pt_br = models.TextField()
    content_en_us = models.TextField(blank=True)
    type = models.TextField(max_length=4, choices=TypeOfContent.choices)
