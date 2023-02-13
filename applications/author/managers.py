from django.db import models
from django.db.models import Q # Para implementar el Or y el And
class AuthorManager(models.Manager):
    ''' Managers para el modelo author '''

    def list_authors(self):
        return self.all()

    def search_author(self, kword):

        # Filtrar por el nombre estrictamente
        # response = self.filter(name = kword)

        # Filtrar por el nombre y el apellido, con que contenga parte del texto
        # response = self.filter(Q(name__icontains = kword) | Q(surnames__icontains = kword))
        
        # El operador And; solo debo usar una ',' y para mayor que el __gt
        # response = self.filter(age__gt = 40, age__lt = 65)
        
        # Consulta de filtrado excluyendo aquellos cuya edad = 70
        response = self.filter(Q(names__icontains = kword) | Q(surnames__icontains = kword)).exclude(age = 68)
        return response