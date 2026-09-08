'''задание 1'''
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)
chislo = random.randint(1, 100)
popytka = 0
while True:
    user_chislo = int(input("введите число от 1 до 100: "))
    popytka += 1
    if user_chislo > chislo:
        print(f"{Fore.RED}Слишком много!")
    elif user_chislo < chislo:
        print(f"{Fore.BLUE}Слишком мало!")
    else:
        print(f"{Fore.GREEN}Поздравляю!")
        print(f"количество попыток: {popytka}")
        break
'''импортируем модуль рандом для генерации случ чисел и колорама для цветного вывода в консоли 
далее из библиотеки колорама импортируем "Fore" чтобы красить текст напрямую без перфикса
далее идет цикл "while true" который будет продолжаться пока мы не угадаем число
каждый раз когда мы вводим число, оно засчитывает +1 к попытке через "+="
соответственно даются подасказки число меньше или больше, и если мы угадаем то нас поздравят, выведут число попыток и завершат цикл
''' 
'''задание 2'''
import time
import os
try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        vremya = time.strftime("%H:%M:%S")
        print(vremya)
        time.sleep(1)
except KeyboardInterrupt:
    print(f"программа прервана")
'''импортируем модули операционной системы и времени
далее через блок "try" мы выполняем инструкцию 
а через блок "except" мы перехватываем исключение из блока "try"
"keyboardinterrupt" прерывает программу через "Ctrl+C"'''
'''задание 3'''
import requests
def check_site(url):
    try:
        otvet = requests.get(url, timeout=15)
        if 200 <= otvet.status_code <= 399:
            print(f"✅Сайт доступен! Код ответа: {otvet.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"❌ Сайт недоступен! Код: {otvet.status_code}")
    except requests.exceptions.Timeout:
     print(f"❌ Ошибка подключения: таймаут / нет сети")
if __name__ == "__main__":
    user_site = input("введите URL сайта: ")
    check_site(user_site)
'''импортируем библиотеку "requests"
через "check_status(url)" принимаем url сайта как аргумент 
через блок "try" проверяем запрос через ".get" с таймаутом 15 сек
если запрос успешен, проверяется код состояния
если от 200 до 399 включительно то сайт считаем доступным, в ином случае он недоступен
блоки "except" ищут исключения, первый ищет ошибки подключения когда сайт недоступен или нет сети
второй ошибки с превышением времени ожидания
if __name__ == "__main__" Этот оператор проверяет, был ли файл запущен напрямую
и в конце у пользователя просят юрл сайта и проверяют через "check_status"
'''

"""Модуль для работы с базой данных склада через PyMySQL."""

import pymysql
import pymysql.cursors


def get_connection():
    """Создает и возвращает подключение к базе данных."""
    return pymysql.connect(
        host="127.0.0.1",
        user="warehouse_user",
        password="CHANGE_ME",
        database="warehouse_db",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False,
    )


def ping():
    """Проверяет соединение с базой данных, запрашивая системную информацию."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT DATABASE() AS db, NOW() AS now, USER() AS user")
            row = cur.fetchone()
            print(row)
            return row
    finally:
        conn.close()


def fetch_products():
    """Получает список всех продуктов и один конкретный продукт по SKU."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # Получение всех продуктов
            cur.execute("SELECT id, sku, name, qty FROM products ORDER BY sku")
            rows = cur.fetchall()
            for row in rows:
                print(row["sku"], row["qty"])

            # Получение одного продукта по SKU
            cur.execute("SELECT * FROM products WHERE sku = %s", ("SKU-002",))
            one = cur.fetchone()
            print("one:", one)
    finally:
        conn.close()


if __name__ == "__main__":
    print("--- Проверка соединения (ping) ---")
    ping()

    print("\n--- Получение данных о продуктах ---")
    fetch_products()
