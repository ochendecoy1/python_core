# . Пользователь одной строкой вводит результаты запуска автотестов через
# пробел, например: PASS FAIL PASS SKIP PASS FAIL. Программа должна
# преобразовать введенную строку в список, подсчитать количество тестов
# каждого типа и вывести общую статистику. Логику подсчета необходимо
# вынести в отдельную функцию get_test_statistics(results), которая
# возвращает результат в виде словаря. Дополнительно программа должна
# вывести процент успешно пройденных тестов относительно общего
# количества тестов.
# Пример вывода:
# Всего тестов: 6
# PASS: 3
# FAIL: 2
# SKIP: 1
# Успешно: 50.0%

testrun = input("Введите результаты прогона: ")
result = testrun.split()


def get_test_statistics(result):
    stats = {}
    for a in result:
        stats[a] = stats.get(a, 0) + 1
    return stats

stats = get_test_statistics(result)
total = len(result)

passed = stats.get("PASS", 0)
failed = stats.get("FAIL", 0)
skipped = stats.get("SKIP", 0)
metric = passed / total * 100

print(stats)
print(f"Всего тестов: {total}")
print(f"PASS: {passed}")
print(f"FAIL: {failed}")
print(f"SKIP: {skipped}")
print(f"Успешно: {metric}%")
