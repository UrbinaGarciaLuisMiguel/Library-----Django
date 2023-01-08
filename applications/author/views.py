from django.shortcuts import render
from django.views.generic import ListView
from .models import Author


class ListAuthorsView(ListView):
    model = Author
    context_object_name = 'list_authors'
    template_name = 'author/list.html'

    def get_queryset(self):
        key_word = self.request.GET.get("kword", "")
        # return Author.objects.list_authors() # Llamado de la función definida en el managers
        return Author.objects.search_author(key_word)