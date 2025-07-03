# 📚 OAU Book Recommender

A hybrid book recommendation system for Obafemi Awolowo University Library. It combines **content-based**, **collaborative filtering**, and **semantic search** using sentence embeddings, TF-IDF, and cosine similarity.

---

## 🚀 Live Demo

Try the full system:

- 🔗 **Frontend UI** (Static HTML):  
  [https://wilsonafolabi.github.io/book-recommender/](https://wilsonafolabi.github.io/book-recommender/)

- ⚙️ **Public API (via Hugging Face Space)**:  
  [https://huggingface.co/spaces/Emeritus-21/oau-book-recommender](https://huggingface.co/spaces/Emeritus-21/oau-book-recommender)

---

## 📌 Features

- 🔍 Search books by **title** or **topic/keywords**
- 🧠 Uses **Sentence Transformers** for semantic matching
- 🧾 Filters and ranks results based on:
  - Ratings
  - Year
  - Page count
  - Genre
- 📦 Fully deployed: Frontend on GitHub Pages, Backend on Hugging Face Spaces

---

## 🛠️ Tech Stack

- **Backend**: FastAPI + Scikit-learn + Sentence Transformers
- **Frontend**: Vanilla HTML/CSS/JS
- **Deployment**:  
  - Frontend → GitHub Pages  
  - Backend API → Hugging Face Spaces

---

## 🧠 How It Works

1. **TF-IDF** vectorizes book metadata (title, author, publisher, genre).
2. **Sentence Transformer** encodes semantic meaning.
3. **Collaborative filtering** uses ratings similarity.
4. All features are combined and passed into **KNN (cosine similarity)** to return top recommendations.

---

## 📡 Public API

You can directly call the backend API from anywhere using the link above.

### Example Endpoint:
```http
GET /recommend/query/?query=python&top_n=5
