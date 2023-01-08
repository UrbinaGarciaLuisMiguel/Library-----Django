from django.db import models
from applications.author.models import Author
from .managers import BookManager, CategoryManager


class Category(models.Model):
    name = models.CharField(max_length = 30)

    objects = CategoryManager()

    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'category_book')
    author   = models.ManyToManyField(Author)
    title    = models.CharField(max_length = 50)
    visits   = models.PositiveIntegerField()
    release_date = models.DateField('Fecha de Lanzamiento')
    front_page   = models.ImageField(upload_to = 'portada')
    
    objects = BookManager()
    
    def __str__(self):
        return self.title
