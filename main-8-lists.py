
print("Завдання 1")
chysla = []
for i in range(5):
    chyslo = int(input("Введіть число: "))
    chysla.append(chyslo)
print(f"Список чисел: {chysla}\n")

print("Завдання 2")
A = [1, 2, 3, 4, 5]
A.pop()
print(f"{A}\n")

print("Завдання 3")
A = []
for i in range(10):
    chyslo = int(input("Введіть число: "))
    A.append(chyslo)
N = int(input("Введіть число для пошуку: "))
kilkist = 0
for chyslo in A:
    if chyslo == N:
        kilkist += 1
print(f"Число {N} зустрічається {kilkist} рази(ів).\n")

print("Завдання 4")
N = int(input("Введіть кількість чисел у списку: "))
A = []
for i in range(N):
    chyslo = int(input("Введіть число: "))
    A.append(chyslo)
print(f"Список у зворотній послідовності: {A[::-1]}\n")

print("Завдання 5")
A = []
for i in range(5):
    chyslo = int(input("Введіть число: "))
    A.append(chyslo)
C = []
for chyslo in A:
    if chyslo > 5:
        C.append(chyslo)
print(f"Числа, що більше 5:{C}\n")

print("Завдання 6")
N = int(input("Введіть кількість чисел: "))
A = []
for i in range(N):
    chyslo = int(input("Введіть число: "))
    A.append(chyslo)

min_chyslo = A[0]
max_chyslo = A[0]
for i in A:
    if i < min_chyslo:
        min_chyslo = i
    if i > max_chyslo:
        max_chyslo = i

print(f"Min = {min_chyslo}.")
print(f"Max = {max_chyslo}.\n")

print("Завдання 7")
text = input("Введіть текст: ")
kilkist = 0
for char in text:
    if char.isdigit():
        kilkist += 1
print(f"Кількість цифр у текстi: {kilkist}")
