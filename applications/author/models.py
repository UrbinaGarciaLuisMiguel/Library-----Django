from django.db import models
# Managers
from .managers import AuthorManager

class Author(models.Model):
        name = models.CharField(max_length = 50)
        surnames = models.CharField(max_length = 50 )
        nationality = models.CharField(max_length = 30 )
        age = models.PositiveIntegerField()

        objects = AuthorManager()
        
        def __str__(self):
                return self.name + " " + self.surnames