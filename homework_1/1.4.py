
a =  "Ivanou Ivan"
b = a.split()

b[0], b[1] = b[1], b[0]
words = " ".join(b)

print(words)