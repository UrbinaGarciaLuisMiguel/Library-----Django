from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListBooksView.as_view(), name = 'list_books'),
    path('detail/<pk>/', views.BookDetailView.as_view(), name = 'detail_book'),
]
