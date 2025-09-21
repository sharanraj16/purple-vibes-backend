from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    """
    Post model related to 'owner' (a User instance).
    Default image set so that we can always reference image.url.
    Added small methods for customization without changing frontend behavior.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, null=True, default='default_post_x90pun')
    image_filter = models.CharField(max_length=32, choices=image_filter_choices, default='normal')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    # --- Backend-only safe enhancements ---
    def snippet(self, length=50):
        """Return a short snippet of the post content for previews."""
        return self.content[:length] + ("..." if len(self.content) > length else "")

    def is_long_post(self, threshold=300):
        """Check if the post content is considered 'long'."""
        return len(self.content) > threshold

    def owner_username(self):
        """Convenience method to get the owner's username."""
        return self.owner.username
