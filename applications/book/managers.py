from django.db import models

class BookManager(models.Manager):
    ''' Managers para el modelo book'''

    # Obtener los libros que contengas title = kword
    def list_books(self, kword):
        response = self.filter (
            title__icontains    = kword
        )
        return response

    # Obtener los libros que contengas title = kword y que cumpla um rango de fecha
    def list_books_by_date(self, kword, date_01, date_02):
        response = self.filter (
            title__icontains    = kword, # Filtrar los titulos
            release_date__range = (date_01, date_02) # Rango de fechas para filtrar los libros
        )
        return response


    def add_author_to_book(self, book_id, author_id):
        book = self.get(id = book_id)
        book.author.add(author_id)
        return book

class CategoryManager(models.Manager):
    ''' Managers para el modelo Categoria '''

    # list de autores por categoria
    def list_category_by_author(self, id_author):
        return self.filter(
            category_book__author__id = id_author
        ).distinct() # 'Distinc' le dice a django que no me repita las categorias


    # Obtener las categorias de libros y la cantidad de libros que hay en la categoria
    def list_category_by_book(self):
        result = self.annotate(
            num_books = self.count('category_book') # Contando numeros de libro que tiene la categoria
        )
        return result

    