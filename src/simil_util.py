import json
import numpy as np
import faiss
import logging

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2') # investigate this model and get performance metrics

# Start of function to get similarities using embeddings between phrases found in text
def find_similar_phrases(phrases, query_embedding, top_k=5):
    
    # Set up search index here
    embedding_dimension = phrase_embedding.shape[1]
    index = faiss.IndexFlatL2(embedding_dimension)

    phrase_embedding = model.encode(phrases, show_progress_bar=True)

    D, I = index.search(np.array([query_embedding]), top_k)
    return [(phrases[idx], D[0][i]) for i, idx in enumerate(I[0])]