# Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить пустым.

file = "numbers.txt"
even_file = "even_file.txt"
odd_file = "odd_file.txt"
even_list = []
odd_list = []

with open(file, "r") as n:
    file_read = n.read().split()
    numbers = [int(x) for x in file_read]

for x in numbers:
    if x % 2 == 0:
        even_list.append(x)
    elif x % 2 != 0:
        odd_list.append(x)

with open(even_file, "w") as f:
    for n in even_list:
        f.write(str(n) + " ")

with open(odd_file, "w") as f:
    for n in odd_list:
        f.write(str(n) + " ")
