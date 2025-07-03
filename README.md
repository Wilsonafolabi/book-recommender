# 📚 OAU Book Recommender

A smart book recommendation system built for students at Obafemi Awolowo University. It recommends books based on topic keywords, ratings, genre, page count, and more — powered by a lightweight semantic search API.

---

## 🚀 Live Demo

- 🌐 **Frontend (UI)**:  
  🔗 [https://wilsonafolabi.github.io/book-recommender/](https://wilsonafolabi.github.io/book-recommender/)

- 🧠 **API (Hugging Face Spaces)**:  
  🔗 [https://emeritus-21-oau-book-recommender.hf.space](https://emeritus-21-oau-book-recommender.hf.space)

- 📑 **API Docs (Swagger UI)**:  
  🔗 [https://emeritus-21-oau-book-recommender.hf.space/docs](https://emeritus-21-oau-book-recommender.hf.space/docs)

- 🧪 **Try an example**:  
  🔗 [Query for "python"](https://emeritus-21-oau-book-recommender.hf.space/recommend/query/?query=python)

---

## 🧠 Features

✅ Search by book topic or title  
✅ Filter by top N, rating, year, or number of pages  
✅ Sort by rating, year, genre, or page count  
✅ Live preview with cover images and links  
✅ Semantic matching using sentence transformers  
✅ No signup or login needed — just search and explore

---

## ⚙️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Backend**: FastAPI, SentenceTransformers, Scikit-learn
- **Model**: Text Embedding via `sentence-transformers/all-MiniLM-L6-v2`
- **Hosting**:
  - Hugging Face Spaces (API)
  - GitHub Pages (Frontend)

---

## 📦 Sample API Usage

### Endpoint
