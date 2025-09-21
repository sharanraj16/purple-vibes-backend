from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' ensures a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} liked {self.post}'

    # --- Backend-only safe enhancements ---
    def toggle(self):
        """
        Placeholder method to toggle like status.
        Actual logic can be implemented in views.
        """
        return f"Toggling like for {self.owner} on post {self.post.id}"

    def is_recent(self, hours=24):
        """Check if the like was created within the last 'hours'."""
        from django.utils import timezone
        return (timezone.now() - self.created_at).total_seconds() < hours * 3600
