from .models              import Book
from django.shortcuts     import render
from django.views.generic import ListView, DetailView

import datetime


class ListBooksView(ListView):
    model               = Book
    context_object_name = 'list_books' # Variable a manipular en el html, or defecto en 'object'
    template_name       = 'book/list.html'

    def get_queryset(self):

        # Captura la información de la request
        key_word = self.request.GET.get("kword", "")  # Palabra filtro
        date_01  = self.request.GET.get("date_01", "") # Fecha 1
        date_02  = self.request.GET.get("date_02", "") # Fecha 2

        # Si hay filtro de fechas
        if date_01 != '' and date_02 != '':
            # Formatear las fecha a año-mes-día
            date_01  = datetime.datetime.strptime(date_01, '%Y-%m-%d').date() 
            date_02  = datetime.datetime.strptime(date_02, '%Y-%m-%d').date()

            return Book.objects.list_books_by_date(key_word, date_01, date_02)
        # Si no hay filtro de fechas
        else:
           return Book.objects.list_books(key_word)

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'