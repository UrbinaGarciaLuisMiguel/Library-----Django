from django.db import models
# Managers
from .managers import AuthorManager

class Author(models.Model):
        names = models.CharField(max_length = 50)
        surnames = models.CharField(max_length = 50 )
        nationality = models.CharField(max_length = 30 )
        age = models.PositiveIntegerField()

        objects = AuthorManager()
        
        class Meta:
                # db_table = 'book' # Nombre de tabla representativa al modelo en la base de datos
                constraints = [
                        models.CheckConstraint(check = models.Q(age__gte = 18 ), name = 'edad_mayor_18')  # restriccion
                ]

        def __str__(self):
                return self.names + " " + self.surnames