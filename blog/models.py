from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=200)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="draft")



    class Meta:
        ordering = ("-published_at",)
    def __str__(self):
        return f"{str(self.id)}-{self.title}"
        




