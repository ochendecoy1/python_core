# Декоратор для логирования автотестов. Напишите декоратор log_test,
# который перед запуском тестовой функции выводит её имя, после
# выполнения сообщает о завершении и выводит полученный результат.
# Декоратор должен поддерживать функции с произвольным количеством
# позиционных и именованных аргументов с помощью *args и **kwargs.
# Используйте functools.wraps(), чтобы сохранить метаданные исходной
# функции.
from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Тест завершён: {func.__name__}")
        print(f"Результат: {result}\n")
        return result
    return wrapper


@log_test
def test_smoke():
    return "OK"

@log_test
def test_login(username, password):
    if username == "buba" and password == "12345":
        return "PASS"
    return "FAIL"

@log_test
def test_timeout(timeout, retries=3):
    if timeout > 0 and retries > 0:
        return "PASS"
    return "FAIL"


test_smoke()
test_login("buba", "12345")
test_login("NeBuba", "676543")
test_timeout(timeout=1.5, retries=2)