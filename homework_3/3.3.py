#  Дан список тестов:
# tests = [
# "test_login",
# "test_logout",
# "test_registration",
# "test_profile",
# "test_payment",
# "test_search"
# ]
# Пользователь вводит количество тестов, которые необходимо запустить.
# Программа должна случайным образом выбрать указанное количество
# уникальных тестов из списка и каждому выбранному тесту случайно
# назначить статус PASS, FAIL или SKIP. Результаты необходимо объединить
# и вывести в виде отчёта. Если пользователь запросил больше тестов, чем
# существует в списке, программа должна вывести сообщение об ошибке.
import random

tests = [
"test_login",
"test_logout",
"test_registration",
"test_profile",
"test_payment",
"test_search"
]

user_input = int(input("Введите количество тестов: "))

if user_input > len(tests):
    print("Слишком много, так не договаривались")

else:
    random_tests = random.sample(tests, user_input)
    statuses = ["PASS", "SKIP", "FAIL", ]

    print("Отчет тестирования:\n")
    for test in random_tests:
        status = random.choice(statuses)
        print(f"{test} - {status}")
