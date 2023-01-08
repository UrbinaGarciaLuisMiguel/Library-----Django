from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
import datetime


class ListBooksView(ListView):
    model = Book
    context_object_name = 'list_books'
    template_name = 'book/list.html'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", "")  # Palabra filtro
        
        date_01  = self.request.GET.get("date_01", "") # Fecha 1
        date_02  = self.request.GET.get("date_02", "") # Fecha 2

        if date_01 != '' and date_02 != '':
            date_01  = datetime.datetime.strptime(date_01, '%Y-%m-%d').date() 
            date_02  = datetime.datetime.strptime(date_02, '%Y-%m-%d').date()
            return Book.objects.list_books_by_date(key_word, date_01, date_02)
        else:
           return Book.objects.list_books(key_word) 