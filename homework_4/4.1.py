# Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку.
#
#

file = "numbers.txt"

with open(file, "r") as n:
    numbers = []
    file_read = n.read().split()
    for a in file_read:
        numbers.append(int(a))

if len(numbers) < 3:
    print("Error, в списке меньше 3 чисел")
else:
    print(f"Первый элемент - {numbers[0]}, второй элемент - {numbers[1]}\n"
          f"Предпоследний элемент - {numbers[-2]}, последний - {numbers[-1]}")