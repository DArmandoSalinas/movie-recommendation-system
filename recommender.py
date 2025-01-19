import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds

# Load datasets
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

# Content-Based Filtering
tfidf = TfidfVectorizer(stop_words='english')
movies['genres'] = movies['genres'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movies_by_title(movie_title, num_recommendations=5):
    indices = movies[movies['title'].str.contains(movie_title, case=False, na=False)].index
    if indices.empty:
        return f"Movie '{movie_title}' not found in the database."
    idx = indices[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    movie_indices = [i[0] for i in sim_scores[1:num_recommendations + 1]]
    return movies[['title']].iloc[movie_indices].to_dict(orient='records')

# Collaborative Filtering
user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
user_item_sparse_matrix = csr_matrix(user_item_matrix.values)
U, sigma, Vt = svds(user_item_sparse_matrix, k=50)
sigma = np.diag(sigma)
predicted_ratings = np.dot(np.dot(U, sigma), Vt)
predicted_ratings_df = pd.DataFrame(predicted_ratings, index=user_item_matrix.index, columns=user_item_matrix.columns)

def recommend_movies_with_names(user_id, num_recommendations=5):
    user_ratings = predicted_ratings_df.loc[user_id].sort_values(ascending=False)
    rated_movies = ratings[ratings['userId'] == user_id]['movieId'].values
    recommendations = user_ratings.drop(rated_movies).head(num_recommendations)
    recommendations = recommendations.reset_index().merge(movies[['movieId', 'title']], on='movieId')
    return recommendations[['title']].to_dict(orient='records')
