# Book Inventory Management System

## Overview

This is a web-based Book Inventory Management System that allows users to manage a collection of books in a library or personal collection. The system enables users to add, filter, search, and delete books. It also supports exporting the inventory to a CSV file, reflecting the current filters and sorting options.

## Features

- **Book Management**: Add, view, edit, and delete books in the inventory.
- **Filtering**: Filter books by title, author, genre, and publication date.
- **Sorting**: Sort books based on multiple criteria such as entry ID, title, author, genre, and publication date in ascending or descending order.
- **CSV Export**: Export the current book inventory to a CSV file, which respects the active filters and sorting options.
- **Responsive Design**: The system is responsive and adjusts to different screen sizes for easy use on both desktops and mobile devices.

## Getting Started

### Prerequisites

Before running this project, make sure you have the following installed:
- Python (version 3.x)
- Django (version 4.x)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/MatthewW05/book-inventory-system.git
    cd book-inventory-system
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the inner project:
    ```bash
    cd LibraryDemo
    ```

4. *(Optional)* Populate the database with sample books:
    ```bash
    python populate_books.py
    ```
    > *Note*: This step will generate approximately 100 random book entries for testing purposes.

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Visit the application in your browser at `http://localhost:8000/view-database`.

### Usage

1. **Adding a Book**: Click the "Add Book" button to open the form. Fill in the book details and submit the form to add the book to the inventory.
2. **Filtering Books**: Use the filter options to filter the books by title, author, genre, or publication date. You can use the search bar to filter by partial title or author (case-insensitive).
3. **Sorting Books**: Choose the sorting criteria (e.g., by entry ID, title, etc.) from the dropdown, and select whether the sorting should be ascending or descending.
4. **Exporting to CSV**: Click the "Download CSV" button to export the current book inventory to a CSV file, including any applied filters or sorting options.

## Design Decisions

### Model:
The application is built around a simple `Inventory` model that holds the basic details of a book, including:
- **Entry ID**: A unique identifier for each book (automatically generated).
- **Title**: The title of the book.
- **Author**: The author(s) of the book.
- **Genre**: The genre/category of the book.
- **Publication Date**: The date when the book was published.
- **ISBN**: The International Standard Book Number (optional).

### Database:
The application uses SQLite3, a lightweight, file-based SQL database provided by Django by default. SQLite3 was chosen for its simplicity and ease of setup, especially for development and small-scale deployments. This ensures compatibility with SQL-based operations like filtering, sorting, and querying data efficiently.

### Challenges:

1. **Dynamic Filtering and Sorting**: One of the challenges was implementing dynamic filtering and sorting of books. I used Django's query parameters (`GET`) to pass the filter and sort values between the views and templates. This ensures that the current filter and sort state is maintained across page reloads and when exporting data to CSV.

2. **Responsive UI**: Another challenge was ensuring the interface is responsive and works well on both desktops and mobile devices. I used Bootstrap for quick and efficient responsive design, but I also had to carefully adjust the layout for filtering and form submissions.

3. **CSV Export with Active Filters and Sorting**: A key challenge was implementing the functionality to export the books to a CSV file while respecting the currently applied filters and sorting options. The export feature needed to gather all the active filter parameters from the URL, apply them to the query, and then export the filtered and sorted data to a CSV file. This required capturing all the dynamic filter and sort parameters from the URL and passing them through the export view to ensure the exported CSV matches what the user sees on the page.

### Screenshots and Visuals
![Book Inventory](DocumentationImages/Screenshot%202024-11-23%20141657.png)
_The table of books._

![Book Filter UI](DocumentationImages/Screenshot%202024-11-23%20142000.png)
_The filter/sorting dropdown._

## Conclusion

This project provides a straightforward solution for managing book inventories in a web-based system. It offers useful features such as filtering, sorting, and exporting to CSV. The system is simple to use and easy to extend with additional features in the future.

---

**Developed by**: Matthew Wong