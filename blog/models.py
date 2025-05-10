from django.db import models
from django.urls import reverse

class Blog(models.Model):
    TITLE = models.CharField(max_length=50)
    AUTHOR = models.ForeignKey(
        "auth.User",
        on_delete = models.CASCADE,
    )
    BODY = models.TextField()

    def __str__(self):
        return self.TITLE
    
    def get_absolut_url(self):
        return reverse("post_detail", kwargs={"pk":self.pk})
    