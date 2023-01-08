from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListBooksView.as_view(), name = 'list_books'),
]
