# Book Suggestion App

## Purpose
This project is a Book Suggestion App that fetches book data from the Google Books API, allowing users to filter books by genre, rating, publication year, and popularity. It also provides a random book suggestion from the filtered list.

## Features
- Select from 6 genres: Thriller, Horror, Sci-Fi, Drama, Fantasy, Romance
- Filter books by:
  - Minimum rating (only available ratings are shown)
  - Publication year (only available years are shown)
  - Sort by popularity
- Display top N books (user chooses how many, 1-40)
- Random book suggestion from filtered results
- Robust error handling for:
  - Network issues
  - Invalid inputs
  - Empty API results

## Libraries Used
- `requests` – For API calls
- `pandas` – For data processing

## Instructions
1. Make sure Python 3.x is installed.
2. Install required libraries:
