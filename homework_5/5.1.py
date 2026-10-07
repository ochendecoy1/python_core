# Дан список результатов автотестов. Для каждого теста известны его
# название, статус выполнения (PASS, FAIL или SKIP) и время выполнения.
# Напишите программу, которая с помощью filter() получает все
# упавшие тесты, с помощью map() формирует список их названий, а с
# помощью reduce() рассчитывает общее время выполнения всех тестов.
# Дополнительно с помощью генератор списка сформируйте список
# названий успешно пройденных тестов. В результате программа должна
# вывести количество тестов каждого статуса, список названий упавших
# тестов, список успешно пройденных тестов и общее время выполнения
# всех тестов.
from functools import reduce

tests = [
    ("test_registration", "PASS", 4.7),
    ("test_login", "PASS", 1.5),
    ("test_search", "SKIP", 0.3),
    ("test_subscribe", "FAIL", 0.8),
    ("test_add_group", "SKIP", 3.2),
    ("test_profile", "PASS", 1.7),
    ("test_logout", "FAIL", 6)
]


failed_test = list(filter(lambda t: t[1] == "FAIL", tests))
failed_names = list(map(lambda t: t[0], failed_test))

total_time = reduce(lambda acc, t: acc + t[2], tests, 0)

passed_names = [t[0] for t in tests if t[1] == "PASS"]

pass_count = 0
fail_count = 0
skip_count = 0

for t in tests:
    if t[1] == "PASS":
        pass_count += 1
    elif t[1] == "FAIL":
        fail_count += 1
    elif t[1] == "SKIP":
        skip_count =+ 1



print("-----------------------Отчет тестирования-----------------------")
print(f"Успешных тестов - {pass_count}")
print(f"Проваленных тестов - {fail_count}")
print(f"Пропущенных тестов - {skip_count}\n")
print(f"Упавшие тесты: ")
for n in failed_names:
    print(f"Тест - {n}")

print(f"\nУспешные тесты: ")
for n in passed_names:
    print(f"Тест - {n}")

print(f"\nОбщая продолжительность тестов - {total_time}")

