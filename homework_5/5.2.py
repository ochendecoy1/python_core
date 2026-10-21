# Создайте JSON-файл с тестовыми пользователями для проверки
# авторизации. Для каждого пользователя должны храниться логин, пароль
# и ожидаемый результат авторизации. Напишите программу, которая
# открывает JSON-файл, загружает данные и выводит информацию о
# каждом тестовом пользователе. Программа должна корректно
# обрабатывать ситуации, когда файл не существует, содержимое файла
# невозможно прочитать как JSON или у пользователя отсутствует
# обязательное поле. Для обработки ошибок используйте try/except,
# соответствующие типы исключений и получение информации об ошибке
# через as e.

import json

file_name = "users.json"

try:
    with open(file_name, "r") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Файл должен содержать список")

    print(f"Загруженно {len(data)} пользователей\n")

    for i, user in enumerate(data, start=1):
        if "login" not in user:
            print(f"ОШИБКА: Пользователь {i} не имеет логина")
            continue
        elif "password" not in user:
            print(f"ОШИБКА: Пользователь {i} не имеет пароля")
            continue
        elif "expected_result" not in user:
            print(f"ОШИБКА: Пользователь {i} не имеет ожидаемого результата")
            continue

        print(f"Пользователь: {i}")
        print(f"Логин: {user['login']}")
        print(f"Пароль: {user['password']}" if user["password"] else "Пароль не указан")
        print(f"Ожидаемый результат: {user['expected_result']}\n")



except FileNotFoundError as e:
    print(f"ОШИБКА: {file_name} не найден")
except json.JSONDecodeError as e:
    print(f"{file_name} невозможно прочитать файл как JSON, ошибка: {e}")
except ValueError as e:
    print(f"ОШИБКА: {e}")
except Exception as e:
    print(f"ОШИБКА: Неизвестная ошибка, подробности: {e}")

        
