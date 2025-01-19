# Movie Recommendation System 🎬📽️

This project demonstrates a robust **Movie Recommendation System** built using machine learning techniques. The system utilizes **Collaborative Filtering**, **Content-Based Filtering**, and a **Hybrid Approach** to provide personalized movie recommendations. It also includes a simple web application powered by Flask to make the recommendations accessible through a user-friendly interface.

## Features
- **Collaborative Filtering**: Leveraging Singular Value Decomposition (SVD) for user-item matrix decomposition, achieving high prediction accuracy.
- **Content-Based Filtering**: Utilizing TF-IDF vectorization and cosine similarity to recommend movies based on genres.
- **Hybrid System**: Combining collaborative and content-based filtering for improved versatility and recommendation quality.
- **Web Application**: Simple Flask app to input a user ID or movie title and receive tailored recommendations.

## Dataset
The project uses the [MovieLens dataset](https://grouplens.org/datasets/movielens/), which includes:
- `movies.csv`: Contains movie IDs, titles, and genres.
- `ratings.csv`: Contains user ratings for movies.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Clone the Repository
```bash
git clone https://github.com/DArmandoSalinas/movie-recommendation-system.git
cd movie-recommendation-system

Install required libraries
pip install -r requirements.txt

Usage
python app.py

Open the browser and go to : http://127.0.0.1:5000/

Explore the jupyter notebook

Project structure:

movie-recommendation-system/
├── app.py                # Flask app code
├── templates/            # HTML templates for the web app
├── static/               # Static files (CSS, JS)
├── MovieRecommendationSystem.ipynb # Jupyter Notebook with model details
├── data/                 # Folder for dataset files
│   ├── movies.csv
│   ├── ratings.csv
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation

Acknowledgments
MovieLens Dataset: GroupLens

Diego Armando Salinas Lugo




