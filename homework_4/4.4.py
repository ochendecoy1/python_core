# Даны два файла произвольного типа. Поменять местами их содержимое.
# Файлы должны быть бинарного типа.

bin_file1 = "data1.png"
bin_file2 = "data2.png"

with open(bin_file1, "rb") as f:
    data1 = f.read()

with open(bin_file2, "rb") as f:
    data2 = f.read()

with open(bin_file1, "wb") as f:
    f.write(data2)

with open(bin_file2, "wb") as f:
    f.write(data1)