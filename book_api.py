# book_api.py
import requests
import pandas as pd

def fetch_books_by_genre(genre, max_results=40):
    """Fetch books from Google Books API for the given genre."""
    query = f"subject:{genre}"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        books = []
        for item in data.get('items', []):
            info = item.get('volumeInfo', {})
            rating = info.get('averageRating')
            year = info.get('publishedDate', 'N/A')[:4] if 'publishedDate' in info else 'N/A'
            books.append({
                'Title': info.get('title', 'N/A'),
                'Authors': ', '.join(info.get('authors', ['Unknown'])),
                'Genre': ', '.join(info.get('categories', ['N/A'])),
                'Publication_Year': year,
                'Rating': rating,
                'Popularity': info.get('ratingsCount', 0)
            })
        return pd.DataFrame(books)
    
    except requests.RequestException as e:
        print(f"⚠️ Network error: {e}")
        return pd.DataFrame()
