from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length = 250)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)