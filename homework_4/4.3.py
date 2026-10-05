# Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.
float_file = "float_numbers.txt"

with open(float_file, "r") as f:
    numbers = [float(x) for x in f.read().split()]

squared_numbers = []
for n in numbers:
    squared_numbers.append(n * n)

with open(float_file, "w") as f:
    for n in squared_numbers:
        f.write(str(n) + "\n")