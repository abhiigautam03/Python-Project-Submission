import pandas as pd
import random
import os
import requests

# ------------------ Google Books API Integration ------------------

def get_books_from_google(query="fiction", max_results=20):
    api_key = "AIzaSyCaJ9wTCBTtkpnUnpSLIdX8AuJBRSy6N2E"  # Your actual API key
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&key={api_key}"

    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data from API:", response.status_code)
        return pd.DataFrame()

    books = response.json().get("items", [])
    if not books:
        return pd.DataFrame()

    book_data = []

    for item in books:
        volume = item.get("volumeInfo", {})

        title = volume.get("title", "Unknown Title")
        authors = ", ".join(volume.get("authors", ["Unknown Author"]))
        published_date = volume.get("publishedDate", "")
        categories = ", ".join(volume.get("categories", ["Unknown Genre"]))
        description = volume.get("description", "No description available")
        popularity = item.get("searchInfo", {}).get("textSnippet", "")
        info_link = volume.get("infoLink", "")

        # Extract year safely
        try:
            year = int(published_date[:4])
        except:
            year = None

        book_data.append({
            "title": title,
            "author": authors,
            "year": year,
            "subject": categories,
            "description": description,
            "popularity": popularity,
            "link": info_link
        })

    return pd.DataFrame(book_data)

# ------------------ Filtering & Suggesting ------------------

def filter_books(df, genre=None, year=None):
    if genre:
        df = df[df["subject"].str.lower().str.contains(genre.lower(), na=False)]

    if year:
        try:
            year = int(year)
            df = df[df["year"] == year]
        except ValueError:
            print("Invalid year entered.")

    return df

def suggest_random_book(df):
    if df.empty:
        print("No books available with the given filters.")
        return

    book = df.sample(1).iloc[0]

    print("\n📚 Book Suggestion:")
    print(f"Title: {book['title']}")
    print(f"Author(s): {book['author']}")
    print(f"Genre(s): {book['subject']}")
    print(f"Published Year: {book['year']}")
    print(f"Description: {book['description'][:300]}...")
    print(f"More Info: {book['link']}")
