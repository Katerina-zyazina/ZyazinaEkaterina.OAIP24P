from flask import Flask, render_template

app = Flask(__name__)

# Список фильмов (добавлены поля genre и description + 2 новых фильма)
movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre": "Фантастика, драма",
        "description": "Группа исследователей отправляется через червоточину в космосе в поисках нового дома для человечества."
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre": "Фантастика, боевик",
        "description": "Хакер Нео узнаёт, что его мир — это симуляция, и присоединяется к борьбе против машин."
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 8.1,
        "genre": "Мультфильм, комедия",
        "description": "Зелёный огр отправляется спасать принцессу, чтобы вернуть своё болото."
    },
    {
        "id": 4,
        "title": "Начало",
        "year": 2010,
        "rating": 8.8,
        "genre": "Фантастика, триллер",
        "description": "Опытный вор внедряется в сны людей, чтобы украсть их секреты. Теперь ему нужно сделать обратное — внедрить идею."
    },
    {
        "id": 5,
        "title": "Побег из Шоушенка",
        "year": 1994,
        "rating": 9.3,
        "genre": "Драма",
        "description": "Несправедливо осуждённый банкир проводит в тюрьме десятилетия, не теряя надежды и достоинства."
    }
]


@app.route("/")
def index():
    """Главная страница — список всех фильмов"""
    return render_template("index.html", movies=movies)


@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    """Страница одного фильма по его ID"""
    for m in movies:
        if m["id"] == movie_id:
            return render_template("movie.html", movie=m)
    # Если фильм не найден — возвращаем 404
    return render_template("movie.html", movie=None), 404


if __name__ == "__main__":
    app.run(debug=True)
