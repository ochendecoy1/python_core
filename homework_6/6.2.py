# Замыкание для проверки времени выполнения. Напишите функцию
# create_time_checker(max_time), которая возвращает вложенную
# функцию для проверки времени выполнения теста. Вложенная функция
# принимает фактическое время выполнения и сообщает, превышен
# установленный лимит или нет. Создайте два независимых замыкания с
# разными значениями max_time и продемонстрируйте их работу.


def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time > max_time:
            return False
        return True
    return check_time


test_times = [0.3, 0.6, 1.5, 2.1, 0.4, 12.5]

fast_check = create_time_checker(1.0)
slow_check = create_time_checker(5.0)

for i, t in enumerate(test_times):
    fast = fast_check(t)
    slow = slow_check(t)

    print(f"Для теста {i} время - {t}")
    print(f"Укладывается ли в 1 секунду - {fast}")
    print(f"Укладывается ли в 5 секунд - {slow}\n")


