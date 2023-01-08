from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListAuthorsView.as_view(), name = 'list_authors'),
]
