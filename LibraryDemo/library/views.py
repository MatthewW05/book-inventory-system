from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Inventory
from django.http import HttpResponse, QueryDict
from django.contrib import messages
import csv
from .genre_info import GENRE_CHOICES

def view_database(request):
    if request.method == "POST":
        # Retrieve data from the form (sent via POST request)
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        publication_date = request.POST.get('publication_date')
        isbn = request.POST.get('isbn')

        # Get the current query string
        query_string = request.META.get('QUERY_STRING', '')
        filter_params = QueryDict(query_string)

        if len(isbn) != 13:
            messages.error(request, "ISBN must be 13 characters long.")
            # Redirect back with filters preserved
            return redirect(f"{reverse('view_database')}?{filter_params.urlencode()}")
        
        elif not isbn.isdigit():
            messages.error(request, "ISBN must contain only digits.")
            # Redirect back with filters preserved
            return redirect(f"{reverse('view_database')}?{filter_params.urlencode()}")
        
        elif Inventory.objects.filter(isbn=isbn).exists():
            messages.error(request, "Book with this ISBN already exists.")
            # Redirect back with filters preserved
            return redirect(f"{reverse('view_database')}?{filter_params.urlencode()}")
        
        elif not title or not author or not genre or not publication_date:
            messages.error(request, "All fields are required.")
            # Redirect back with filters preserved
            return redirect(f"{reverse('view_database')}?{filter_params.urlencode()}")

        # Create and save the new book entry
        new_book = Inventory(title=title, author=author, genre=genre, 
                        publication_date=publication_date, isbn=isbn)
        new_book.save()

        # Add a success message
        messages.success(request, "New book added successfully!")
    
    # Retrieve filter parameters
    filter_title = request.GET.get('filter_title', '').strip()
    filter_author = request.GET.get('filter_author', '').strip()
    filter_genre = request.GET.get('filter_genre', '').strip()
    filter_date = request.GET.get('filter_date', '').strip()

    # Retrieve sorting parameters
    sort_by = request.GET.get('sort_by', 'title')  # Default to sorting by title
    sort_dir = request.GET.get('sort_dir', 'asc')  # Default to ascending order

    # Filter the queryset based on parameters
    books = Inventory.objects.all()

    if filter_title:
        books = books.filter(title__startswith=filter_title)
    if filter_author:
        books = books.filter(author__icontains=filter_author)
    if filter_genre:
        books = books.filter(genre=filter_genre)
    if filter_date:
        books = books.filter(publication_date=filter_date)
    
    sort_by = request.GET.get('sort_by', 'entry_id')  # Default to 'entry_id'
    sort_dir = request.GET.get('sort_dir', 'desc')  # Default to 'desc'
    
    if sort_by in ['entry_id', 'title', 'author', 'genre', 'publication_date']:
        books = books.order_by(f'{sort_by}' if sort_dir == 'asc' else f'-{sort_by}')
    
    context = {
        "books": books,
        "filters": request.GET,
        "GENRE_CHOICES": GENRE_CHOICES,
    }

    return render(request, 'view_database.html', context)

def export_books_csv(request):
    # Retrieve filter parameters
    filter_title = request.GET.get('filter_title', '').strip()
    filter_author = request.GET.get('filter_author', '').strip()
    filter_genre = request.GET.get('filter_genre', '').strip()
    filter_date = request.GET.get('filter_date', '').strip()

    # Retrieve sorting parameters
    sort_by = request.GET.get('sort_by', 'entry_id')  # Default sort field
    sort_dir = request.GET.get('sort_dir', 'desc')    # Default sort direction

    # Start with all books in the database
    books = Inventory.objects.all()

    # Apply filters if they are provided
    if filter_title:
        books = books.filter(title__startswith=filter_title)
    if filter_author:
        books = books.filter(author__icontains=filter_author)
    if filter_genre:
        books = books.filter(genre=filter_genre)
    if filter_date:
        books = books.filter(publication_date=filter_date)

    if sort_by in ['entry_id', 'title', 'author', 'genre', 'publication_date']:
        books = books.order_by(f'{sort_by}' if sort_dir == 'asc' else f'-{sort_by}')

    # Create an HTTP response with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books_inventory.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(['Entry ID', 'Title', 'Author', 'Genre', 'Publication Date', 'ISBN'])

    # Write book data rows
    for book in books:
        writer.writerow([book.entry_id, book.title, book.author, book.genre, book.publication_date, book.isbn])

    return response

def delete_book(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Inventory, entry_id=book_id)
        book.delete()

        # Get the current query string
        query_string = request.META.get('QUERY_STRING', '')
        filter_params = QueryDict(query_string)

        # Redirect back with filters preserved
        return redirect(f"{reverse('view_database')}?{filter_params.urlencode()}")