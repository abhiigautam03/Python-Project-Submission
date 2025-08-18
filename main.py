# main.py
from book_api import fetch_books_by_genre
from book_filter import filter_books, display_books, suggest_random_book

GENRES = {
    "Thriller": "Thriller",
    "Horror": "Horror",
    "Sci-Fi": "Science Fiction",
    "Drama": "Drama",
    "Fantasy": "Fantasy",
    "Romance": "Romance"
}

def main():
    print("📚 Welcome to the Book Suggestion App!\n")
    
    # Genre selection
    print("Select a genre:")
    for idx, g in enumerate(GENRES.keys(), 1):
        print(f"{idx}. {g}")
    genre_choice = int(input("Enter number (1-6): ").strip())
    genre_name = list(GENRES.keys())[genre_choice - 1]
    genre_query = GENRES[genre_name]
    
    # Fetch books
    df = fetch_books_by_genre(genre_query)
    if df.empty:
        print("⚠️ No books fetched from API.")
        return
    
    # Show available ratings
    available_ratings = sorted(df['Rating'].dropna().unique())
    if available_ratings:
        print("\n⭐ Minimum Rating (available):", available_ratings)
        rating_input = input("Choose rating (or press Enter to skip): ").strip()
        rating_choice = float(rating_input) if rating_input else None
    else:
        rating_choice = None
    
    # Show available publication years
    available_years = sorted(df['Publication_Year'].dropna().unique())
    if available_years:
        print("\n📅 Publication Year (available):", available_years)
        year_input = input("Choose year (or press Enter to skip): ").strip()
        year_choice = int(year_input) if year_input else None
    else:
        year_choice = None
    
    # Popularity sort
    sort_pop_input = input("🔥 Sort by Popularity? (yes/no): ").strip().lower()
    sort_by_pop = sort_pop_input == "yes"
    
    # Filter books (now includes genre)
    filtered_df = filter_books(
        df,
        rating_choice=rating_choice,
        year_choice=year_choice,
        sort_by_pop=sort_by_pop,
        genre=genre_query
    )
    
    # Ask how many books to show
    max_books_input = input("\n📘 How many book suggestions? (1-40, default 10): ").strip()
    max_books = int(max_books_input) if max_books_input else 10
    if max_books > 40:
        max_books = 40
    elif max_books < 1:
        max_books = 1
    
    # Display top books
    display_books(filtered_df, max_results=max_books)
    
    # Random book suggestion
    random_choice = input("\nDo you want a random book suggestion? (yes/no): ").strip().lower()
    if random_choice == "yes":
        suggest_random_book(filtered_df)

if __name__ == "__main__":
    main()
