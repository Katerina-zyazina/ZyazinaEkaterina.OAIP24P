from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Данные для проверки логина (в реальном проекте храните в базе данных)
VALID_USERNAME = "admin"
VALID_PASSWORD = "12345"

@app.route('/')
def login_page():
    """Главная страница с формой входа"""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Обработка POST запроса с формой входа"""
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        # Если данные верны, перенаправляем на страницу /me
        return redirect(url_for('me'))
    else:
        # Если данные неверны, возвращаемся на страницу входа с сообщением об ошибке
        return render_template('login.html', error="Неверный логин или пароль")

@app.route('/me')
def me():
    """Страница с приветствием"""
    return render_template('me.html')

@app.route('/about')
def about():
    """Страница 'Обо мне'"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)