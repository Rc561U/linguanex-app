from django.db import models


class Application(models.Model):
    title = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120)
    publishedYear = models.IntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.title
