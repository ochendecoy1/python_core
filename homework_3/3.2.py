# Есть два списка:
# test_cases = ["Login", "Registration", "Checkout", "Logout"]
# statuses = ["PASS", "FAIL", "PASS", "SKIP"]
# Необходимо с помощью zip() объединить название каждого тест-кейса с
# его статусом. Создайте функцию print_report(test_cases, statuses),
# которая принимает два списка и выводит отчёт в формате Login — PASS.
# После формирования отчета программа должна определить количество
# успешных и неуспешных тестов и сообщить, можно ли считать тестовый
# запуск успешным: если есть хотя бы один FAIL, запуск считается
# неуспешным.

test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

def print_report(test_cases, statuses):

    report = (zip(test_cases, statuses))
    for case, status in report:
        print(f"{case}" + " -- " + f"{status}")

passed_case = 0
failed_case = 0

for status in statuses:
    if status == "PASS":
        passed_case += 1
    elif status == "FAIL":
        failed_case += 1

print("\nРезультат прогона: \n")

print_report(test_cases,statuses)

if failed_case > 0:
    print(f"\nПрогон провален, присутствуют упавшие тесты в количестве - {failed_case}.")
    print(f"Статистика: PASS - {passed_case}, FAIL - {failed_case}")
else:
    print(f"\nВсе тесты прошли успешно")
    print(f"Статистика: PASS - {passed_case}, FAIL - {failed_case}")
