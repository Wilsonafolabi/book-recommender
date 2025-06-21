from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch

app = Flask(__name__)
model = SentenceTransformer("book-recommender_model")
data = pd.read_csv("oau_books_cleaned2.csv")

# Combine gfor metadata for semantic search
sentences = data.apply(
    lambda row: f"Title: {row['Title']}, Author: {row['Author']}, Publisher: {row['Publisher']}",
    axis=1
).tolist()

# book encoding
corpus_embeddings = model.encode(sentences, convert_to_tensor=True)

# Recommendation 
def get_recommendations(query, top_n=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    top_results = torch.topk(scores, k=top_n)

    results = []
    for idx in top_results.indices:
        i = idx.item()
        results.append({
            "title": data.iloc[i]['Title'],
            "author": data.iloc[i]['Author'],
            "link": data.iloc[i].get('Link', '#'),
            "image_url": data.iloc[i].get('Image URL', 'https://via.placeholder.com/150')
        })
    return results


@app.route("/")
def index():
    return render_template("index.html")  # refer to the index oo

# API endpoints
@app.route("/recommend", methods=["POST"])
def recommend():
    content = request.get_json()
    query = content.get("query", "")
    top_n = content.get("top_n", 5)
    results = get_recommendations(query, top_n)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
