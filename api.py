from flask import Flask, request, jsonify
from recommender import recommendMovies
from sentiment import getEmotionsList

app = Flask(__name__)

@app.route('/movies/basedOnUserText', methods=['POST'])
def recommendMoviesBasedOnUserText():
    data = request.get_json()
    emotions = getEmotionsList(data['user_response'])
    emotion = max(emotions, key=emotions.get).strip()
    movies = recommendMovies(emotion)s
    response_data = {'movies': movies}
    return jsonify(response_data)

@app.route('/movies/basedOnUserEmotion', methods=['POST'])
def recommendMoviesBasedOnUserEmotion():
    data = request.get_json()
    movies = recommendMovies(data['user_response'])
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)