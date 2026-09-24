# Результаты автотестов. Пользователь вводит количество выполненных
# автотестов, а затем по очереди результат каждого теста: PASS, FAIL или
# SKIP. Программа должна подсчитать количество тестов с каждым
# статусом и вывести итоговую статистику. Если присутствует хотя бы один
# FAIL, необходимо сообщить о наличии упавших тестов; если FAIL
# отсутствуют - сообщить об успешном прохождении выполненных тестов.
# Любой неизвестный статус необходимо пропустить и не учитывать в
# статистике

input_count = int(input("Сколько было тестов: "))

pass_count = 0
fail_count = 0
skip_count = 0

for i in range(input_count):
    test_status = str(input("Введите результат теста: ")).upper()
    if test_status == "PASS":
        pass_count += 1
    elif test_status == "FAIL":
        fail_count += 1
    elif test_status == "SKIP":
        skip_count += 1
    else:
        print("Некорректный статус")

print(f"PASS: {pass_count}")
print(f"FAIL: {fail_count}")
print(f"SKIP: {skip_count}")

if fail_count > 0:
    print("Есть упавшие тесты")
else:
    print("Все тесты пройдены")

