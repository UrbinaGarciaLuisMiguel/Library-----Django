from django.db import models
from django.contrib.postgres.search import TrigramSimilarity

class BookManager(models.Manager):
    ''' Managers para el modelo book'''

    # # La función list_books es mejorada en la linea 18
    # # Obtener los libros que contengas title = kword
    # def list_books(self, kword):
    #     response = self.filter (
    #         title__icontains    = kword
    #     )
    #     return response

    
    def list_books(self, kword):

        # Codigo para crear una extensión en postgres desde la shell y poder realizar la busqueda por diagramación
        # \c db_library
        # CREATE INDEX book_title_idx ON book_book USING GIN(title gin_trgm_ops);
        # CREATE EXTENSION pg_trgm;

        if kword:
            response = self.filter (
                title__trigram_similar = kword,                
            )
            return response
        else:
            response = self.all()[:10]
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

    def number_loans_by_book(self):
        result = self.aggregate(
            number_loans = models.Count('book_loan')
        )
        return result
                         

class CategoryManager(models.Manager):
    ''' Managers para el modelo Categoria '''

    # list de autores por categoria
    def list_category_by_author(self, id_author):
        return self.filter(
            category_book__author__id = id_author
        ).distinct() # 'Distinc' le dice a django que no me repita las categorias


    # Obtener las categorias existentes y vinculadas a los libros,
    # Es decir, solo retornará las categorias en las cuales halla libros registrados
    def list_category_by_book(self):
        result = self.annotate(
            num_books = models.Count('category_book') # Contando numeros de libro que tiene la categoria
        )
        return result

    