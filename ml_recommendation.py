import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors

class MovieRecommendationSystem:
    def __init__(self):
        # Load dataset (replace this with your actual dataset)
        self.data = pd.read_csv('movie_data.csv')  # Sample movie dataset
        
        # Preprocess data (feature engineering, scaling, etc.)
        self.processed_data = self.preprocess_data(self.data)
        
        # Train model
        self.model = self.train_model(self.processed_data)
    
    def preprocess_data(self, data):
        # Preprocess data as needed (e.g., encode categorical variables, scale numerical features)
        # This method will depend on the structure of your dataset
        return data
    
    def train_model(self, data):
        # Split data into train and test sets
        X_train, X_test = train_test_split(data, test_size=0.2, random_state=42)
        
        # Train a recommendation model (e.g., collaborative filtering)
        model = NearestNeighbors(n_neighbors=5, algorithm='auto')
        model.fit(X_train)
        
        return model
    
    def recommend_movies(self, user_preferences):
        # Recommend movies based on user preferences
        # This method will use the trained model to generate recommendations
        
        # Example: For now, return top 5 movies from the dataset
        return self.data['movie_title'][:5].tolist()
