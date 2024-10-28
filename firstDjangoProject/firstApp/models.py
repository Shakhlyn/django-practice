from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title