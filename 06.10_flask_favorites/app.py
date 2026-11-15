from flask import Flask, render_template, redirect, session
import random

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Необходим для работы сессий

# Список фильмов с genre и rating (самостоятельная часть)
movies = [
    {"id": 1, "title": "Интерстеллар", "year": 2014, "genre": "Фантастика", "rating": 8.7},
    {"id": 2, "title": "Матрица", "year": 1999, "genre": "Фантастика, боевик", "rating": 8.5},
    {"id": 3, "title": "Шрек", "year": 2001, "genre": "Мультфильм, комедия", "rating": 8.1},
    {"id": 4, "title": "Джентльмены", "year": 2019, "genre": "Криминал, комедия", "rating": 8.6},
    {"id": 5, "title": "Начало", "year": 2010, "genre": "Фантастика, триллер", "rating": 8.8},
]


@app.route("/")
def index():
    """Главная страница со списком фильмов"""
    favorites = session.get("favorites", [])
    return render_template("index.html", movies=movies, favorites_count=len(favorites), favorites=favorites)


@app.route("/add/<int:movie_id>")
def add_favorite(movie_id):
    """Добавление фильма в избранное"""
    if "favorites" not in session:
        session["favorites"] = []

    favorites = session["favorites"]

    # Проверка: если фильм уже есть, не добавляем повторно
    if movie_id not in favorites:
        favorites.append(movie_id)
        session["favorites"] = favorites

    return redirect("/")


@app.route("/favorites")
def favorites():
    """Страница избранных фильмов"""
    favorite_ids = session.get("favorites", [])
    favorite_movies = [movie for movie in movies if movie["id"] in favorite_ids]
    return render_template("favorites.html", movies=favorite_movies)


@app.route("/remove/<int:movie_id>")
def remove_favorite(movie_id):
    """Удаление фильма из избранного"""
    favorites = session.get("favorites", [])
    if movie_id in favorites:
        favorites.remove(movie_id)
        session["favorites"] = favorites
    return redirect("/favorites")


@app.route("/clear")
def clear_favorites():
    """Очистка всего избранного"""
    session["favorites"] = []
    return redirect("/favorites")


@app.route("/random")
def random_movie():
    """Дополнительное задание: случайный фильм"""
    movie = random.choice(movies)
    return render_template("random.html", movie=movie)


if __name__ == "__main__":
    app.run(debug=True)