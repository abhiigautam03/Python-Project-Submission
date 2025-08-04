import requests
import pandas as pd

def get_books_from_google(query, max_results=10, year_filter=None):
    api_key = 'AIzaSyCaJ9wTCBTtkpnUnpSLIdX8AuJBRSy6N2E'  # Replace with your valid API key if needed
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        books = []
        for idx, item in enumerate(data.get("items", []), 1):
            info = item.get("volumeInfo", {})
            pub_date = info.get("publishedDate", "N/A")
            pub_year = pub_date[:4] if len(pub_date) >= 4 else "Unknown"

            # Filter by year if provided
            if year_filter and pub_year != year_filter:
                continue

            books.append({
                "Ranking": idx,
                "Title": info.get("title", "N/A"),
                "Authors": ", ".join(info.get("authors", ["Unknown"])),
                "Genres": ", ".join(info.get("categories", ["Unknown"])),
                "Publication Year": pub_year,
                "Popularity (Ratings Count)": info.get("ratingsCount", 0),
                "Average Rating": info.get("averageRating", "N/A"),
                "More Info": info.get("infoLink", "")
            })

        if not books:
            print(f"\n❗ No books found for '{query}' in year {year_filter}. Try without the year filter.\n")
            return pd.DataFrame()

        # Sort by popularity
        books.sort(key=lambda x: x["Popularity (Ratings Count)"], reverse=True)
        for i, book in enumerate(books, 1):
            book["Ranking"] = i

        df = pd.DataFrame(books)

        print(f"\n📚 Top {len(books)} books for query: '{query}'")
        for book in books:
            print(f"{book['Ranking']}. {book['Title']} by {book['Authors']}")
            print(f"   Genres: {book['Genres']}")
            print(f"   Published: {book['Publication Year']}")
            print(f"   Rating: {book['Average Rating']} ({book['Popularity (Ratings Count)']} ratings)")
            print(f"   More Info: {book['More Info']}\n")

        return df

    except requests.RequestException as e:
        print("❌ Error fetching data:", e)
        return pd.DataFrame()
