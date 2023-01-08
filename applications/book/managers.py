from django.db import models

class BookManager(models.Manager):
    ''' Managers para el modelo book'''

    def list_books(self, kword):
        response = self.filter (
            title__icontains    = kword, 
            release_date__range = ('1000-01-01', '3000-01-01')
        )
        return response

    def list_books_by_date(self, kword, date_01, date_02):
        response = self.filter (
            title__icontains    = kword, 
            release_date__range = (date_01, date_02)
        )
        return response