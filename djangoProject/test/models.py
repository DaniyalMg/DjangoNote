from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'