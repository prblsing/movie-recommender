import faiss
import pickle
from sentence_transformers import SentenceTransformer

# File paths for embeddings, index, and TF-IDF vectorizer
embeddings_file = 'embeddings.pkl'
index_file = 'index.faiss'
tfidf_vectorizer_file = 'tfidf_vectorizer.pkl'
metadata_file = 'movie_metadata.pkl'

# Load precomputed embeddings, FAISS index, TF-IDF vectorizer, and movie metadata
with open(embeddings_file, 'rb') as f:
    sentence_embeddings = pickle.load(f)
with open(tfidf_vectorizer_file, 'rb') as f:
    tfidf_vectorizer = pickle.load(f)
with open(metadata_file, 'rb') as f:
    movie_metadata = pickle.load(f)
index = faiss.read_index(index_file)


def comprehensive_search(query, k=5):
    """
    Performs a comprehensive search for movies based on a user query.

    Args:
    - query (str): The user query string.
    - k (int): The number of top results to return.

    Returns:
    - DataFrame: The top k movies that match the query along with their release years.
    """

    # Generate embeddings for the query using TF-IDF and Sentence-BERT
    tfidf_query_embedding = tfidf_vectorizer.transform([query]).toarray().astype('float32')
    sentence_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    sbert_query_embedding = sentence_model.encode([query]).astype('float32')

    # Normalize the query embeddings for accurate cosine similarity search
    faiss.normalize_L2(tfidf_query_embedding)
    faiss.normalize_L2(sbert_query_embedding)

    # Perform the search in the FAISS index
    _, sbert_indices = index.search(sbert_query_embedding, k)

    # Retrieve the top k results from the movie metadata
    top_indices = sbert_indices[0][:k]
    top_movies = movie_metadata.iloc[top_indices]

    # Return only the relevant columns (6 columns) to match the renaming step
    return top_movies[['Series_Title', 'Genre', 'Released_Year', 'Overview', 'Director', 'Star1']], top_movies[
        'Released_Year']
