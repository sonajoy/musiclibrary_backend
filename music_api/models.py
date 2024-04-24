from django.db import models


from django.contrib.auth.models import User



from django.db import models

class song(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # New description field
    image = models.ImageField(upload_to='book_images/', blank=True)  # New image field

    def _str_(self):
        return self.title


