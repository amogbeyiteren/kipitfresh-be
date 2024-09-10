import uuid
from django.db import models

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    tags = models.CharField(max_length=200)
    is_featured_story = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
