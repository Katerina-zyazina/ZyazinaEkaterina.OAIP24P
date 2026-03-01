from flask import Flask, render_template_string

app = Flask(__name__)

# HTML шаблон прямо в коде (для простоты)
TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Калькулятор</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .result { font-size: 24px; margin: 20px; color: blue; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Калькулятор</h1>
    
    {% if error %}
        <div class="error">{{ error }}</div>
    {% else %}
        <div class="result">
            {{ num1 }} {{ op }} {{ num2 }} = {{ result }}
        </div>
    {% endif %}
    
    <p><a href="/">Назад</a></p>
</body>
</html>
'''

@app.route('/')
def home():
    return '''
    <h1>Калькулятор на Flask</h1>
    <p>Введите в адресной строке:</p>
    <p><code>/число/операция/число/</code></p>
    <br>
    <p><b>Примеры:</b></p>
    <ul>
        <li><a href="/7/*/2/">7 * 2</a> → 14</li>
        <li><a href="/10/+/5/">10 + 5</a> → 15</li>
        <li><a href="/9/-/4/">9 - 4</a> → 5</li>
        <li><a href="/6.5/:/2/">6.5 : 2</a> → 3.25</li>
        <li><a href="/2/^/3/">2 ^ 3</a> → 8</li>
        <li><a href="/5/:/0/">5 : 0</a> → Ошибка</li>
    </ul>
    '''

@app.route('/<path:num1>/<op>/<path:num2>/')
def calculate(num1, op, num2):
    try:
        # Преобразуем строки в числа
        num1 = float(num1)
        num2 = float(num2)
        
        # Выполняем операцию
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == ':':
            if num2 == 0:
                return render_template_string(TEMPLATE, error="Ошибка: деление на ноль!")
            result = num1 / num2
        elif op == '^':
            result = num1 ** num2
        else:
            return render_template_string(TEMPLATE, error=f"Ошибка: неизвестная операция '{op}'")
        
        # Возвращаем результат
        return render_template_string(TEMPLATE, num1=num1, num2=num2, op=op, result=result)
        
    except ValueError:
        return render_template_string(TEMPLATE, error="Ошибка: введите корректные числа")
    except Exception as e:
        return render_template_string(TEMPLATE, error=f"Ошибка: {str(e)}")

if __name__ == '__main__':
    print("=" * 50)
    print("Запуск калькулятора...")
    print("Откройте браузер и перейдите по адресу: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)