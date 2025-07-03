# 📚 OAU Book Recommender

A hybrid book recommendation system built with FastAPI and Sentence Transformers. It combines content-based filtering (TF-IDF + semantic embeddings) and collaborative filtering (ratings-based) to suggest academic books to students.

---

## 🚀 Features

- 🔍 Recommend books by title or by topic query
- 💬 Smart text matching using Sentence Transformers
- 📊 Ratings-aware recommendations
- 🎯 Filtering and sorting (by rating, year, genre, pages)
- 🌐 Public API and fully responsive frontend
- 📦 Deployed Demo: [Click to try it!](https://wilsonafolabi.github.io/book-recommender/)

---

## 🧠 Tech Stack

- **Backend**: FastAPI, Scikit-learn, Sentence-Transformers
- **Frontend**: HTML + CSS + Vanilla JavaScript
- **Model**: SentenceTransformer + TF-IDF + KNN + Cosine Similarity
- **Deployment**:
  - Frontend: GitHub Pages
  - Backend (optional): Render or Hugging Face Spaces

---

## 📁 Project Structure

```bash
book-recommender/
│
├── api/
│   └── main.py            # FastAPI app
│   └── oau_books.csv      # Book dataset with ratings and metadata
│
├── frontend/
│   └── index.html         # UI for user interaction
│
├── model/
│   └── vectorizer.pkl     # TF-IDF Vectorizer (optional)
│   └── sentence_model/    # SentenceTransformer embeddings
│
├── README.md
└── requirements.txt
