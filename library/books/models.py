from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 250)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    borrower = models.ForeignKey(User, null=True,blank=True, on_delete=models.SET_NULL)

    