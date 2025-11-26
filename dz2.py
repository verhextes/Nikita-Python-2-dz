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
