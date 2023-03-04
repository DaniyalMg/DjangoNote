from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
