import requests
import pandas as pd

def fetch_books_by_genre(genre="science_fiction", limit=20, filename=None):
    """
    Fetches books from Open Library API by genre.
    Saves to a CSV file (custom or default).
    """
    url = f"https://openlibrary.org/subjects/{genre}.json?limit={limit}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        books = []

        for book in data.get("works", []):
            books.append({
                "title": book.get("title"),
                "author": book["authors"][0]["name"] if book.get("authors") else "Unknown",
                "year": book.get("first_publish_year", "Unknown"),
                "rating": book.get("rating", "N/A"),
                "subject": genre
            })

        df = pd.DataFrame(books)

        if not filename:
            filename = f"{genre}_books.csv"

        df.to_csv(filename, index=False)
        print(f"{len(books)} books saved to {filename}")
        return df

    except requests.RequestException as e:
        print("Network error:", e)
        return pd.DataFrame()
