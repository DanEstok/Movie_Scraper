import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.sparse.linalg import svds
import numpy as np

class MovieRecommendationSystem:
    def __init__(self, data_path='movie_data.csv'):
        self.data = pd.read_csv(data_path)
        self.user_movie_matrix = self.create_user_movie_matrix(self.data)
        self.U, self.sigma, self.Vt = svds(self.user_movie_matrix, k=min(self.user_movie_matrix.shape)-1)
        self.sigma = np.diag(self.sigma)

    def create_user_movie_matrix(self, data):
        user_movie_matrix = data.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
        return user_movie_matrix

    def recommend_movies(self, user_id, num_recommendations=5):
        user_ratings = self.user_movie_matrix.loc[user_id]
        user_ratings = user_ratings.values.reshape(1, -1)
        predicted_ratings = np.dot(np.dot(self.U, self.sigma), self.Vt)
        user_predicted_ratings = predicted_ratings[user_id - 1]

        # Filter out movies already rated by the user
        unrated_movies_idx = np.where(user_ratings == 0)[1]
        user_predicted_ratings = user_predicted_ratings[unrated_movies_idx]

        # Get indices of top-rated movies
        recommended_movie_indices = np.argsort(user_predicted_ratings)[::-1][:num_recommendations]

        # Get corresponding movie titles
        recommended_movies = self.data.loc[self.data['movie_id'].isin(recommended_movie_indices + 1), 'movie_title'].tolist()

        return recommended_movies

# Example usage:
# recommendation_system = MovieRecommendationSystem()
# recommendations = recommendation_system.recommend_movies(user_id=1)
# print(recommendations)
