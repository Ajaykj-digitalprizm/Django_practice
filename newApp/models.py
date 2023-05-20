from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    vote_count = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
