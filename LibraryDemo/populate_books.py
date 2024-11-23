import os
import random
from datetime import datetime, timedelta
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryDemo.settings")
import django

django.setup()

from library.models import Inventory  # Replace with your app name
from library.genre_info import GENRE_CHOICES  # Import GENRE_CHOICES

# Constants
AUTHORS = [
    "John Smith", "Jane Doe", "Mark Twain", "Emily Brontë", "George Orwell",
    "Agatha Christie", "J.K. Rowling", "J.R.R. Tolkien", "Stephen King", "Virginia Woolf"
]
TITLES = [
    "The Adventures of Sherlock Holmes", "1984", "To Kill a Mockingbird",
    "The Great Gatsby", "Pride and Prejudice", "Moby-Dick", "The Catcher in the Rye",
    "The Lord of the Rings", "Harry Potter", "War and Peace", "Crime and Punishment",
    "Brave New World", "The Hobbit", "Anna Karenina", "Ulysses", "Jane Eyre",
    "The Picture of Dorian Gray", "Frankenstein", "Dracula", "Wuthering Heights"
]
GENRES = [choice[0] for choice in GENRE_CHOICES]  # Extract genre values from GENRE_CHOICES


# Helper function to generate a random publication date
def random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def populate_books(n=100):
    print(f"Adding {n} books to the database...")
    
    # Define the date range for publication dates
    start_date = datetime(1900, 1, 1)
    end_date = datetime(2023, 1, 1)
    
    for _ in range(n):
        title = random.choice(TITLES)
        author = random.choice(AUTHORS)
        genre = random.choice(GENRES)
        publication_date = random_date(start_date, end_date)
        isbn = f"{random.randint(1000000000000, 9999999999999)}"  # Random 13-digit ISBN

        # Create and save book entry
        book = Inventory.objects.create(
            title=title,
            author=author,
            genre=genre,
            publication_date=publication_date,
            isbn=isbn
        )
        print(f"Added: {book.title} by {book.author}")

    print("Database population complete.")


if __name__ == "__main__":
    populate_books()
