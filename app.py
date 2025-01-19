from flask import Flask, request, jsonify, render_template
from recommender import recommend_movies_by_title, recommend_movies_with_names

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_title = data.get('movie_title', '')
    user_id = data.get('user_id', None)
    
    if user_id:
        recommendations = recommend_movies_with_names(int(user_id))
        return jsonify(recommendations)
    elif movie_title:
        recommendations = recommend_movies_by_title(movie_title)
        return jsonify(recommendations)
    else:
        return jsonify({'error': 'Provide a valid user_id or movie_title!'})

if __name__ == '__main__':
    app.run(debug=True)
