from ast import keyword
from django.db import models

# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Text(models.Model):
    text = models.TextField(max_length=200)

class Author(models.Model):
    keyword = models.ForeignKey

class Created_date(models.Model):
    datetime = models.DateTimeField

class Published_date(models.Model):
    datetime = models.DateTimeField