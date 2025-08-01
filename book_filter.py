import pandas as pd
import random
import os

def load_all_books(folder="."):
    """
    Load and combine all *_books.csv files in the given folder.
    Returns a single pandas DataFrame.
    """
    all_files = [f for f in os.listdir(folder) if f.endswith("_books.csv")]
    dataframes = []

    for file in all_files:
        df = pd.read_csv(os.path.join(folder, file))
        dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df


def filter_books(df, genre=None, year=None):
    """
    Filter books by genre and/or year.
    """
    if genre:
        df = df[df["subject"].str.lower() == genre.lower()]

    if year:
        try:
            year = int(year)
            df = df[df["year"] == year]
        except ValueError:
            print("Invalid year entered.")

    return df


def suggest_random_book(df):
    """
    Randomly pick a book and return its details.
    """
    if df.empty:
        print("No books available with the given filters.")
        return None

    random_book = df.sample(1).iloc[0]

    print("\n📚 Book Suggestion:")
    print(f"Title: {random_book['title']}")
    print(f"Author: {random_book['author']}")
    print(f"Year: {random_book['year']}")
    print(f"Genre: {random_book['subject']}")
