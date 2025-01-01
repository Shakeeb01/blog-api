from django.db import models

# Our Models.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    # String Representation for better readability.
    def _str__(self):
        return self.title
