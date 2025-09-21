from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = CloudinaryField('image', default='default_profile_rqdzyf')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

    # --- Backend-only safe enhancements ---
    def display_name(self):
        """Return name if set, otherwise username."""
        return self.name if self.name else self.owner.username

    def short_bio(self, length=50):
        """Return a truncated version of the profile content."""
        return self.content[:length] + ("..." if len(self.content) > length else "")

    def has_custom_image(self):
        """Check if the user has uploaded a custom profile image."""
        return self.image.name != 'default_profile_rqdzyf'


# Signal to create Profile automatically when a new User is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
