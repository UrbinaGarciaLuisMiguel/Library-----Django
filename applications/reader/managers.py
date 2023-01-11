from django.db import models

class LoanManager(models.Manager):
    ''' Managers para el modelo loan '''

    # Edades promedio de los autores que prestaron determinado libro
    def book_average_age(self, id_book):
        result = self.filter(book__id = id_book).aggregate(average_age = models.Avg('reader__age'))  # reader el campo de modelo 'Loan' y id es campo del modelo 'reader', 
        return result                                                                               # Es decir,  hace referencia al foreingkey 'reader' y accede a su campo id ('reader__id')
        
    # cantidad de veces prestado cada libro 
    def number_book_borrowed(self):
        # En values colocamos en base a qué queremos que annotate agrupe
        result = self.values('book').annotate(num_borrowed = models.Count('book'))
        return result