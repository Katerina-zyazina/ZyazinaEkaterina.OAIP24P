from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Пример данных для тестирования
    # Можно менять значения для проверки разных случаев
    a = 1
    b = 3
    c = 2
    return render_template('index.html', a=a, b=b, c=c)

# Добавим маршрут для тестирования разных значений через URL
@app.route('/<int:a>/<int:b>/<int:c>/')
def test_numbers(a, b, c):
    return render_template('index.html', a=a, b=b, c=c)

if __name__ == '__main__':
    app.run(debug=True)