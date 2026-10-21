# Создайте собственное исключение InvalidTestStatusError,
# наследуемое от Exception. Напишите функцию, которая принимает статус
# теста и проверяет его значение. Допустимыми считаются только PASS,
# FAIL и SKIP. Если передан любой другой статус, функция должна с
# помощью raise создать InvalidTestStatusError и передать в него
# сообщение с некорректным значением. В основной программе
# обработайте это исключение через try/except и выведите понятное
# сообщение пользователю. Проверьте программу как с корректными, так и
# с некорректными статусами.

class InvalidTestStatusError(Exception):
    pass


def validate_status(status):
    allowed_status = {"PASS", "FAIL", "SKIP"}
    if status not in allowed_status:
        raise InvalidTestStatusError(
            f"Некорректный статус: {status}. "
            f"Допустимые статусы: {allowed_status}")
    print(f"Статус {status} валиден!")

test_cases = ["PASS", "FAIL", "SKIP", "ERROR", "pass"]
for case in test_cases:
    try:
        validate_status(case)
    except InvalidTestStatusError as e:
        print(f"Ошибка: {e}")