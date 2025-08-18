# book_filter.py
import pandas as pd

def filter_books(df, rating_choice=None, year_choice=None, sort_by_pop=False, genre=None):
    """Filter books, guaranteed to return results if possible."""
    if df.empty:
        return df
    
    filtered_df = df.copy()
    
    # Filter by genre (partial match, case-insensitive)
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    
    # Filter by rating
    if rating_choice is not None:
        filtered_df.loc[:, 'Rating'] = filtered_df['Rating'].fillna(0).astype(float)
        filtered_df = filtered_df[filtered_df['Rating'] >= rating_choice]
    
    # Filter by publication year
    if year_choice is not None:
        filtered_df.loc[:, 'Publication_Year'] = filtered_df['Publication_Year'].astype(str)
        filtered_df = filtered_df[filtered_df['Publication_Year'] == str(year_choice)]
    
    # Sort by popularity
    if sort_by_pop:
        filtered_df = filtered_df.sort_values(by="Popularity", ascending=False)
    
    # Fallback to original df if filtering gives nothing
    if filtered_df.empty:
        filtered_df = df.sort_values(by="Popularity", ascending=False) if sort_by_pop else df
        
    return filtered_df

def display_books(df, max_results=10):
    """Display books nicely with sequential numbering."""
    if df.empty:
        print("\n⚠️ No books found from API.")
        return

    for idx, (_, row) in enumerate(df.head(max_results).iterrows(), start=1):
        print(f"\n📚 Book {idx}")
        print(f"Title           : {row['Title']}")
        print(f"Author(s)       : {row['Authors']}")
        print(f"Genre(s)        : {row['Genre']}")
        print(f"Publication Year: {row['Publication_Year']}")
        print(f"Rating          : {row['Rating']}")
        print(f"Popularity      : {row['Popularity']}")

def suggest_random_book(df):
    """Pick a random book from filtered DataFrame."""
    if df.empty:
        print("⚠️ No books available for random suggestion.")
        return
    book = df.sample(1).iloc[0]
    print("\n🎲 Random Book Suggestion")
    print(f"Title           : {book['Title']}")
    print(f"Author(s)       : {book['Authors']}")
    print(f"Genre(s)        : {book['Genre']}")
    print(f"Publication Year: {book['Publication_Year']}")
    print(f"Rating          : {book['Rating']}")
    print(f"Popularity      : {book['Popularity']}")
