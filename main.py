from book_api import get_books_from_google
import pandas as pd

def main():
    print("📚 Welcome to the Book Suggestion App!")
    
    query = input("🔍 Enter a keyword, genre, or author: ").strip()
    count = input("📘 How many book suggestions do you want? (max 40): ").strip()
    year = input("📅 Filter by publication year (optional): ").strip()

    try:
        max_results = min(int(count), 40)
    except:
        max_results = 10

    year_filter = year if year.isdigit() else None

    df = get_books_from_google(query, max_results, year_filter)

    if not df.empty:
        save = input("💾 Save results to CSV? (yes/no): ").strip().lower()
        if save in ["yes", "y"]:
            filename = f"{query}_books.csv"
            df.to_csv(filename, index=False)
            print(f"✅ Results saved to {filename}")

if __name__ == "__main__":
    main()
