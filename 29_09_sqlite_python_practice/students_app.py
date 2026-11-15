import sqlite3

def init_db(conn):
    """Создание таблицы и добавление начальных данных"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            group_name TEXT NOT NULL,
            grade INTEGER NOT NULL,
            age INTEGER
        )
    ''')
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        initial_students = [
            ('Иванов Иван', 'ИСП-101', 5, 19),
            ('Петров Пётр', 'ИСП-101', 4, 18),
            ('Сидоров Алексей', 'ИСП-102', 3, 20),
            ('Смирнова Анна', 'ИСП-102', 5, 19),
            ('Кузнецов Максим', 'ИСП-101', 4, 18)
        ]
        cursor.executemany("INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)", initial_students)
        conn.commit()

def get_int_input(prompt):
    """Защита от ввода букв вместо чисел"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Ошибка: введите целое число.")

def print_students(students):
    """Красивый вывод списка"""
    if not students:
        print("📭 Студенты не найдены.")
        return
    print(f"{'ID':<5} | {'ФИО':<25} | {'Группа':<10} | {'Оценка':<6} | {'Возраст'}")
    print("-" * 65)
    for s in students:
        print(f"{s[0]:<5} | {s[1]:<25} | {s[2]:<10} | {s[3]:<8} | {s[4]}")

def main():
    conn = sqlite3.connect('students.db')
    init_db(conn)
    cursor = conn.cursor()

    while True:
        print("\n===== УЧЁТ СТУДЕНТОВ =====")
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Найти студентов по группе")
        print("4. Найти студентов по оценке")
        print("5. Изменить оценку")
        print("6. Удалить студента")
        print("7. [Доп] Статистика")
        print("0. Выход")
        
        choice = input("Выберите пункт меню: ").strip()

        if choice == '1':
            cursor.execute("SELECT * FROM students")
            print_students(cursor.fetchall())

        elif choice == '2':
            name = input("Введите ФИО студента: ")
            group_name = input("Введите название группы: ")
            grade = get_int_input("Введите оценку: ")
            age = get_int_input("Введите возраст: ")
            cursor.execute("INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)", 
                           (name, group_name, grade, age))
            conn.commit()
            print("✅ Студент добавлен!")

        elif choice == '3':
            group_name = input("Введите название группы: ")
            cursor.execute("SELECT * FROM students WHERE group_name = ?", (group_name,))
            print_students(cursor.fetchall())

        elif choice == '4':
            grade = get_int_input("Введите оценку: ")
            cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
            print_students(cursor.fetchall())

        elif choice == '5':
            student_id = get_int_input("Введите ID студента: ")
            new_grade = get_int_input("Введите новую оценку: ")
            cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
            conn.commit()
            print("✅ Оценка изменена!" if cursor.rowcount > 0 else "❌ ID не найден.")

        elif choice == '6':
            student_id = get_int_input("Введите ID студента для удаления: ")
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("✅ Студент удалён. Оставшиеся:")
                cursor.execute("SELECT * FROM students")
                print_students(cursor.fetchall())
            else:
                print("❌ ID не найден.")

        elif choice == '7':
            cursor.execute("SELECT AVG(grade) FROM students")
            avg_grade = cursor.fetchone()[0]
            print(f"\n📊 Средняя оценка: {avg_grade:.2f}")
            cursor.execute("SELECT group_name, COUNT(*) FROM students GROUP BY group_name")
            for group in cursor.fetchall():
                print(f"   - {group[0]}: {group[1]} чел.")

        elif choice == '0':
            print("👋 До свидания!")
            break
        else:
            print("⚠️ Неверный пункт меню.")

    conn.close()

if __name__ == "__main__":
    main()
