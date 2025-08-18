# 📚 Book Suggestion App

A **Python-based interactive book suggestion application** that fetches book data from the **Google Books API**. Filter books by rating, publication year, popularity, and genre, and export your favorite suggestions to a CSV file.

---

## ✨ Features

* 🚀 Fetches book data dynamically from Google Books API
* 🔍 Filter books by:

  * Genre
  * Minimum rating
  * Publication year
  * Popularity
* 🖥️ Display top N book suggestions in the terminal
* 📁 Export displayed suggestions to a CSV file
* 🎲 Random book suggestion feature for spontaneous discovery

---

## 🛠️ Getting Started

### Prerequisites

* Python 3.10+ installed
* `pip` installed

### Install Dependencies

```bash
pip install -r requirements.txt
```

### 🖥️ Run the App

```bash
python main.py
```

Follow the prompts:

1. Choose a genre
2. Select minimum rating (optional)
3. Select publication year (optional)
4. Sort by popularity? (yes/no)
5. Enter the number of book suggestions

✅ Top suggestions will appear in the terminal.
💾 A CSV file of the displayed books will be saved in the `output/` folder.

---

## 📄 CSV Export

* **File name:** `book_suggestions.csv`
* **Location:** `output/` folder
* Contains the exact books displayed in the terminal

---

## 🎲 Random Book Suggestion

After displaying your top books, you can request a random suggestion from the filtered list. The app will show **one randomly chosen book** from the current filtered dataset.

---

## 👨‍💻 Author

**Abhishek Gautam**
📧 [gauabh@amazon.com](mailto:gauabh@amazon.com)
