from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    test_dict_args = {
        "color": "Brown",
        "animal_one": "Fox",
        "animal_two": "Dog",
        "movie_one": "Matrix",
        "movie_two": "Batman",
        "movie_three": "The Godfather",
        "apple_count": 12,
        "orange_count": 18,
        "firstname": "Ashish",
        "lastname": "Pant"
    }
    return render_template("home.html", **test_dict_args)


@app.route("/movie")
def movie():
    movies = [
        "The Matrix",
        "Batman",
        "Spider Man - No Way Home"
    ]
    car = {
        "brand": "Maruti Suzuki",
        "model": "Brezza",
        "year": "2023"
    }
    return render_template("movie.html", movies=movies, car=car)


@app.route("/game")
def game():
    return render_template("game.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
