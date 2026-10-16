# Рекурсивный подсчет результатов тестов. Дан список результатов
# автотестов со статусами PASS, FAIL и SKIP. Напишите рекурсивную
# функцию, которая подсчитывает количество тестов со статусом PASS.
# Функция должна обрабатывать список с помощью рекурсии.
# Использовать циклы for и while нельзя

def pass_recurcive(result, index=0):
    if index == len(result):
        return 0

    current = 1 if result[index] == "PASS" else 0
    return current + pass_recurcive(result, index + 1)



test1 = ["PASS","FAIL","PASS","SKIP","PASS"]
print(f"В первом списке успешных тестов - {pass_recurcive(test1)}")

test2 = ["FAIL","SKIP","FAIL"]
print(f"В первом списке успешных тестов - {pass_recurcive(test2)}")

test3 = ["PASS","PASS","PASS"]
print(f"В первом списке успешных тестов - {pass_recurcive(test3)}")