from django.db import models
from applications.book.models import Book

class Reader(models.Model):

    names      = models.CharField(max_length = 50)
    surnames   = models.CharField(max_length = 50)
    natinality = models.CharField(max_length = 30)
    age        = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.name + " - " + self.surnames




class Loan(models.Model):

    reader      = models.ForeignKey(Reader, on_delete = models.CASCADE)
    book        = models.ForeignKey(Book, on_delete = models.CASCADE)
    loan_date   = models.DateField()
    return_date = models.DateField(blank = True, null = True)
    returned    = models.BooleanField()

    def __str__(self):
        return self.book.title