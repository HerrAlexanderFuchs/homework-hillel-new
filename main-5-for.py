
n = int(input("Введiть кiлькiсть зiрочок: "))
n += 1

print("Трикутник №1")
i = 1
for i in range(i, n):
    print("*" * (n - i))
print()

print("Трикутник №2")
i = 1
for i in range(i, n):
    print("*" * i)
print()

print("Трикутник №3")
i = 1
for i in range(i, n):
    print(" " * (i - 1) + "*" * (n - i))
print()

print("Трикутник №4")
i = 1
for i in range(i, n):
    print(" " * (n - (i+1)) + "*" * i)
