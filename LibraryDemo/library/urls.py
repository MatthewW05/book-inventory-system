from django.urls import path
from . import views

urlpatterns = [
    path('view-database/', views.view_database, name='view_database'),
    path('export-csv/', views.export_books_csv, name='export_books_csv'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]