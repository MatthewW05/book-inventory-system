from django.db import models
from .genre_info import GENRE_CHOICES

class Inventory(models.Model):  # The class name can differ; table name will be set manually.
    entry_id = models.AutoField(primary_key=True)                       # Auto-incrementing Entry ID.
    title = models.CharField(max_length=255)                            # Title of the book.
    author = models.CharField(max_length=255)                           # Author name.
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)      # Genre of the book.
    publication_date = models.DateField()                               # Publication date.
    isbn = models.CharField(max_length=13, unique=True)                 # ISBN, unique to each book.

    class Meta:
        db_table = 'Inventory'  # Explicitly set the database table name.

    def __str__(self):
        return self.title