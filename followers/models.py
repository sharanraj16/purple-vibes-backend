from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'owner' and 'followed'.
    'owner' is a User that is following a User.
    'followed' is a User that is followed by 'owner'.
    'unique_together' ensures a user can't follow the same user twice.
    """
    owner = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} follows {self.followed}'

    # --- Backend-only safe enhancements ---
    def is_self_following(self):
        """Check if the owner is following themselves (edge case)."""
        return self.owner == self.followed

    def follow_duration_days(self):
        """Return how many days the follow relationship has existed."""
        from django.utils import timezone
        delta = timezone.now() - self.created_at
        return delta.days

    def toggle_follow(self):
        """Placeholder for future follow/unfollow logic."""
        return f"Toggling follow status for {self.owner} -> {self.followed}"
