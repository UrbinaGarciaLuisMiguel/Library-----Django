from django.db import models
from applications.book.models import Book

from .managers import LoanManager

class Reader(models.Model):
    ''' Modelo de Lector '''

    names = models.CharField(max_length = 50)
    surnames = models.CharField(max_length = 50 )
    nationality = models.CharField(max_length = 30 )
    age = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id) + " - " + self.names + " " + self.surnames


class Loan(models.Model):
    ''' Modelo de Prestamo '''

    reader      = models.ForeignKey(Reader, on_delete = models.CASCADE)
    book        = models.ForeignKey(Book, on_delete = models.CASCADE, related_name = 'book_loan')
    loan_date   = models.DateField()
    return_date = models.DateField(blank = True, null = True)
    returned    = models.BooleanField()

    objects = LoanManager()

    def __str__(self):
        return self.book.title