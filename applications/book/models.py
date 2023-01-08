from django.db import models
from applications.author.models import Author
from .managers import BookManager
class Category(models.Model):

    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    author   = models.ManyToManyField(Author)
    title    = models.CharField(max_length = 50)
    visits   = models.PositiveIntegerField()
    release_date = models.DateField('Fecha de Lanzamiento')
    front_page   = models.ImageField(upload_to = 'portada')
    
    objects = BookManager()
    
    def __str__(self):
        return self.title
