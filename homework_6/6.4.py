#  Декоратор повторного запуска. Напишите декоратор с параметром
# retry(count), который повторно запускает декорируемую функцию
# указанное количество раз, пока функция не вернет True. Перед каждой
# попыткой необходимо выводить её номер. Если функция вернула True,
# дальнейшие попытки выполнять не нужно. Декоратор должен
# поддерживать передачу позиционных и именованных аргументов через
# *args и **kwargs.
from functools import wraps
import random


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # начинаю с одного
            for attempt in range(1, count + 1):
                print(f"Попытка {attempt} из {count}")
                result = func(*args, **kwargs)
                if result is True:
                    print("функция выполнена")
                    return result

                print("Не удалось, пробуем ещё раз")

            print("Попытки исчерпаны")
            return False

        return wrapper

    return decorator

@retry(count=3)
def test_pass():
    return True

# по статистике, уж на третий раз обязана прокнуть
@retry(count=10)
def test_random():
    i = int(random.choice(range(1, 10)))
    if i > 5:
        return True
    else:
        return False

@retry(count=3)
def test_fail():
    return False

# тест сравнения двух аргументов
@retry(count=2)
def test_with_args(x, y):
    if x > y:
        return True
    else:
        return False


print(f"Итог успешного {test_pass()}\n")
print(f"Итог провального {test_fail()}\n")
print(f"Итог рандомного {test_random()}\n")
print(f"Как пойдет {test_with_args(4, 5)}\n")
print(f"И тут {test_with_args(8, 3)}")