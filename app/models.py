from django.db import models

class Notes(models.Model):
    author = models.CharField(max_length=30)
    topic = models.CharField(max_length=40)
    description = models.TextField()
    def __str__(self):
        return self.author