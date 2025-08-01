from book_filter import load_all_books, filter_books, suggest_random_book

try:
    df = load_all_books()

    if df.empty:
        print("No book data found. Make sure CSV files are in the folder.")
        exit()

    genre = input("Enter a genre to filter by (or press Enter to skip): ").strip()
    year = input("Enter a year to filter by (or press Enter to skip): ").strip()

    filtered = filter_books(df, genre=genre if genre else None, year=year if year else None)

    suggest_random_book(filtered)

except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
except Exception as e:
    print("Something went wrong:", e)
