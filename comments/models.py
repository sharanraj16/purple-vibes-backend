from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content[:50]  # Show a snippet for better readability

    # --- Backend-only safe enhancements ---
    def is_long_comment(self, threshold=200):
        """Check if the comment is longer than a threshold (for moderation or UI hints)."""
        return len(self.content) > threshold

    def snippet(self, length=50):
        """Return a short preview of the comment."""
        return self.content[:length] + ("..." if len(self.content) > length else "")

    def updated_recently(self, hours=24):
        """Check if the comment was updated within the last 'hours' hours."""
        from django.utils import timezone
        return (timezone.now() - self.updated_at).total_seconds() < hours * 3600
