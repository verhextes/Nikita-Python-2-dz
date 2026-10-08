"""Стартовый файл: обработка данных на Python. Реализуйте функции вместо raise NotImplementedError.

Запуск: python starter.py
"""
import inspect


# ============ ДАННЫЕ (менять не нужно) ============
students = [
    {"id": 1, "name": "Анна",  "city": "Москва", "age": 19},
    {"id": 2, "name": "Борис", "city": "Казань", "age": 22},
    {"id": 3, "name": "Вера",  "city": "Москва", "age": 20},
    {"id": 4, "name": "Глеб",  "city": "Тверь",  "age": 18},
    {"id": 5, "name": "Дарья", "city": "Казань", "age": 21},
    {"id": 6, "name": "Егор",  "city": "Москва", "age": 23},
    {"id": 7, "name": "Жанна", "city": "Тверь",  "age": 19},
    {"id": 8, "name": "Захар", "city": "Москва", "age": 20},
]

courses = [
    {"id": 1, "title": "Python",     "hours": 40},
    {"id": 2, "title": "SQL",        "hours": 30},
    {"id": 3, "title": "Алгоритмы",  "hours": 50},
    {"id": 4, "title": "Статистика", "hours": 35},
]

grades = [
    {"student_id": 1, "course_id": 1, "score": 92},
    {"student_id": 1, "course_id": 2, "score": 85},
    {"student_id": 1, "course_id": 3, "score": 78},
    {"student_id": 2, "course_id": 1, "score": 70},
    {"student_id": 2, "course_id": 2, "score": 88},
    {"student_id": 3, "course_id": 1, "score": 95},
    {"student_id": 3, "course_id": 2, "score": 91},
    {"student_id": 3, "course_id": 4, "score": 84},
    {"student_id": 4, "course_id": 1, "score": 60},
    {"student_id": 5, "course_id": 2, "score": 73},
    {"student_id": 5, "course_id": 3, "score": 81},
    {"student_id": 5, "course_id": 4, "score": 90},
    {"student_id": 6, "course_id": 1, "score": 88},
    {"student_id": 6, "course_id": 2, "score": 79},
    {"student_id": 6, "course_id": 3, "score": 93},
    {"student_id": 7, "course_id": 3, "score": 67},
    {"student_id": 7, "course_id": 4, "score": 72},
]


# ============ ЗАДАНИЯ: реализуйте функции ============

def moscow_students(students):
    """Задание 1. Список имён студентов из Москвы (в исходном порядке)."""
    raise NotImplementedError


def sorted_cities(students):
    """Задание 2. Отсортированный список городов без повторов."""
    raise NotImplementedError


def average(values):
    """Задание 3. Среднее значений, округлённое до 2 знаков; для пустого списка 0.0."""
    raise NotImplementedError


def high_scores(students, courses, grades, min_score):
    """Задание 4. Список кортежей (имя, название курса, оценка) для оценок >= min_score."""
    raise NotImplementedError


def count_by_city(students):
    """Задание 5. Словарь {город: количество студентов}."""
    raise NotImplementedError


def took_both(grades, course_a, course_b):
    """Задание 6. Отсортированный список id студентов с оценками по обоим курсам."""
    raise NotImplementedError


def no_grades(students, grades):
    """Задание 7. Отсортированный список имён студентов без единой оценки."""
    raise NotImplementedError


def top_students(students, grades, n):
    """Задание 8. n лучших студентов: список кортежей (имя, средний балл)."""
    raise NotImplementedError


def best_score_per_course(courses, grades):
    """Задание 9. Словарь {название курса: максимальная оценка}."""
    raise NotImplementedError


class Gradebook:
    """Задание 10. Журнал оценок."""

    def __init__(self, grades):
        raise NotImplementedError

    def add(self, student_id, course_id, score):
        raise NotImplementedError

    def average_for(self, student_id):
        raise NotImplementedError


def older_than(students, min_age):
    """Задание 11. Генератор имён студентов с возрастом >= min_age."""
    raise NotImplementedError


def report(students, grades):
    """Задание 12. Текстовый отчёт о средних баллах (многострочная строка)."""
    raise NotImplementedError


# ============ САМОПРОВЕРКА (менять не нужно) ============

def check_10():
    source = [dict(g) for g in grades]
    book = Gradebook(source)
    book.add(8, 1, 77)
    avg = book.average_for(8)
    try:
        book.add(8, 2, 120)
        message = None
    except ValueError as exc:
        message = str(exc)
    return avg, message, len(source)


def check_11():
    gen = older_than(students, 21)
    is_gen = inspect.isgenerator(gen)
    first = next(gen)
    rest = list(gen)
    return is_gen, first, rest


CHECKS = [
    (1, lambda: moscow_students(students), ['Анна', 'Вера', 'Егор', 'Захар']),
    (2, lambda: sorted_cities(students), ['Казань', 'Москва', 'Тверь']),
    (3, lambda: (average([92, 85, 78]), average([])), (85.0, 0.0)),
    (4, lambda: high_scores(students, courses, grades, 90), [('Анна', 'Python', 92), ('Вера', 'Python', 95), ('Вера', 'SQL', 91), ('Дарья', 'Статистика', 90), ('Егор', 'Алгоритмы', 93)]),
    (5, lambda: count_by_city(students), {'Москва': 4, 'Казань': 2, 'Тверь': 2}),
    (6, lambda: took_both(grades, 1, 2), [1, 2, 3, 6]),
    (7, lambda: no_grades(students, grades), ['Захар']),
    (8, lambda: top_students(students, grades, 3), [('Вера', 90.0), ('Егор', 86.67), ('Анна', 85.0)]),
    (9, lambda: best_score_per_course(courses, grades), {'Python': 95, 'SQL': 91, 'Алгоритмы': 93, 'Статистика': 90}),
    (10, lambda: check_10(), (77.0, 'оценка должна быть от 0 до 100', 17)),
    (11, lambda: check_11(), (True, 'Борис', ['Дарья', 'Егор'])),
    (12, lambda: report(students, grades), 'Студент    Средний\nВера         90.00\nЕгор         86.67\nАнна         85.00\nДарья        81.33\nБорис        79.00\nЖанна        69.50\nГлеб         60.00\nВсего студентов с оценками: 7'),
]


def run_checks():
    passed = 0
    for num, func, expected in CHECKS:
        try:
            got = func()
        except NotImplementedError:
            print(f"Задание {num:>2}: не реализовано")
            continue
        except Exception as exc:
            print(f"Задание {num:>2}: ОШИБКА {type(exc).__name__}: {exc}")
            continue
        if got == expected:
            passed += 1
            print(f"Задание {num:>2}: OK")
        else:
            print(f"Задание {num:>2}: НЕВЕРНО")
            print(f"    получено:  {got!r}")
            print(f"    ожидалось: {expected!r}")
    print(f"\nПройдено заданий: {passed} из {len(CHECKS)}")


if __name__ == "__main__":
    run_checks()
