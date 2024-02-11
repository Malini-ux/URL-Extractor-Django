# models.py
from django.db import models

class Article(models.Model):
    link = models.URLField()
    link_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.link
