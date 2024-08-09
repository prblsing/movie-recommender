import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# File paths for embeddings, index, and TF-IDF vectorizer
embeddings_file = 'embeddings.pkl'
tfidf_vectorizer_file = 'tfidf_vectorizer.pkl'
metadata_file = 'movie_metadata.pkl'

# Load precomputed embeddings, TF-IDF vectorizer, and movie metadata
with open(embeddings_file, 'rb') as f:
    sentence_embeddings = pickle.load(f)
with open(tfidf_vectorizer_file, 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
with open(metadata_file, 'rb') as f:
    movie_metadata = pickle.load(f)

def comprehensive_search(query, sbert_weight=0.7, k=5):
    """
    Performs a comprehensive search for movies based on a user query using cosine similarity.

    Args:
    - query (str): The user query string.
    - sbert_weight (float): The weight given to Sentence-BERT based search.
    - k (int): The number of top results to return.

    Returns:
    - DataFrame: The top k movies that match the query along with their release years.
    """

    # Generate embeddings for the query using Sentence-BERT
    sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    query_embedding = sentence_model.encode([query]).astype('float32')

    # Compute cosine similarity between the query and all movie embeddings
    similarities = cosine_similarity(query_embedding, sentence_embeddings)[0]

    # Get top k most similar movies, usually 5
    top_indices = similarities.argsort()[-k:][::-1]
    top_movies = movie_metadata.iloc[top_indices]

    # Return the relevant columns
    return top_movies[['Series_Title', 'Genre', 'Released_Year', 'Overview', 'Director', 'Star1']], top_movies['Released_Year']
