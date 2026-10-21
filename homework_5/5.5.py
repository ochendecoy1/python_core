# Создайте программу для формирования отчёта по результатам
# автоматизированного тестирования. Исходные данные программа
# должна получать из JSON-файла, в котором для каждого теста указаны
# название, статус и время выполнения. Программа должна определить
# общее количество тестов, количество тестов со статусами PASS, FAIL и
# SKIP, сформировать список упавших тестов, определить самый
# длительный тест и рассчитать суммарное время выполнения. При
# обработке данных необходимо использовать минимум один генератор
# списка, lambda, filter() и reduce(). Работу с файлом и входными
# данными необходимо защитить с помощью try/except: программа
# должна корректно обрабатывать отсутствие файла, некорректный JSON и
# неправильную структуру тестовых данных. Сформированный итоговый
# отчёт необходимо сохранить в отдельный JSON-файл.


import json
from functools import reduce
input_file = "tests.json"
output_file = "report.json"

try:
    with open(input_file, "r") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Файл должен содержать список")

    requirements_fields = ["name", "status", "time"]
    for i, test in enumerate(data):
        if not isinstance(test, dict):
            raise ValueError(f"Элемент {i} должен быть словарем")

        for field in requirements_fields:
            if field not in test:
                raise ValueError(f"Отсутствует поле {field} в элементе {i}")
    # Всего тестов
    total_tests = len(data)
    # Тесты каждого статуса
    pass_count = len(list(filter(lambda x: x["status"] == "PASS", data)))
    fail_count = len(list(filter(lambda x: x["status"] == "FAIL", data)))
    skip_count = len(list(filter(lambda x: x["status"] == "SKIP", data)))

    failed_tests = [test["name"] for test in data if test["status"] == "FAIL"]

    # Самый долгий тест
    longest_test = reduce(
        lambda a, b: a if a["time"] >= b["time"] else b,
        data
    )

    # Итоговое время прогона
    total_time = reduce(lambda acc, t: acc + t["time"], data, 0)

    report = {
        "total_tests": total_tests,
        "passed_tests": pass_count,
        "failed_tests": fail_count,
        "skipped_tests": skip_count,
        "failed_names": failed_tests,
        "longest_test":{
            "name": longest_test["name"],
            "time": longest_test["time"]
        },
        "total_time": total_time
    }

    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)

except FileNotFoundError:
    print(f"Файл {input_file} не найден")
except json.JSONDecodeError as e:
    print(f"Файл не является JSON-ом: {e}")
except ValueError as e:
    print(f"Некорректная структура данных: {e}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")



