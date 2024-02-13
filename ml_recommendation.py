import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

class MovieRecommendationSystem:
    def __init__(self, data_path='movie_data.csv'):
        """
        Initialize the Movie Recommendation System.

        Parameters:
        - data_path: Path to the movie data CSV file.
        """
        self.data = pd.read_csv(data_path)
        self.user_movie_matrix = self.create_user_movie_matrix(self.data)
        self.U, self.sigma, self.Vt = svds(self.user_movie_matrix, k=min(self.user_movie_matrix.shape)-1)
        self.sigma = np.diag(self.sigma)

    def create_user_movie_matrix(self, data):
        """
        Create the user-movie ratings matrix.

        Parameters:
        - data: DataFrame containing user-movie ratings.

        Returns:
        - user_movie_matrix: User-movie ratings matrix.
        """
        user_movie_matrix = data.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
        return user_movie_matrix

    def recommend_movies(self, user_id, num_recommendations=5):
        """
        Recommend movies for a given user.

        Parameters:
        - user_id: ID of the user for whom movies are recommended.
        - num_recommendations: Number of movies to recommend.

        Returns:
        - recommended_movies: List of recommended movie titles.
        """
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
