# Создайте собственный модуль test_data.py. В нём реализуйте функции
# generate_login(), generate_age(), generate_status() и
# generate_user().
# generate_user() должна использовать остальные функции и возвращать
# готового тестового пользователя в виде словаря.
# Создайте второй файл main.py. Импортируйте в него созданный модуль,
# запросите у пользователя количество необходимых тестовых
# пользователей и сформируйте их список. После генерации выведите
# пользователей и статистику по статусам ACTIVE, BLOCKED и INACTIVE

from test_data import generate_user


user_input = int(input("Количество необходимых пользователей: "))

users = []

for u in range(user_input):
    user = generate_user()
    users.append(user)

print("Сгенерированные пользователи:\n")

for user in users:
    print(f"Логин - {user['login']}, Возраст - {user['age']}, Статус - {user['status']}.")

active_users = 0
blocked_users = 0
inactive_users = 0

for user in users:
    status = user['status']
    if status == "ACTIVE":
        active_users += 1
    elif status == "BLOCKED":
        blocked_users += 1
    elif status == "INACTIVE":
        inactive_users += 1

print("\n----------Статистика по статусам пользователей----------\n")
print(f"Активных пользователей - {active_users}")
print(f"Неактивных пользователей - {inactive_users}")
print(f"Заблокированных пользователей - {blocked_users}")
