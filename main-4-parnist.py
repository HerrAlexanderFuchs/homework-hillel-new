
a = int(input("Введiть цiле число: "))

# Вариант 1, решение "в лоб"
if a % 2 != 0 and a > 20:
    print("Not Weird")
elif a % 2 != 0:
    print("Weird")
elif a % 2 == 0 and 2 <= a <= 5:
    print("Not Weird")
elif a % 2 == 0 and 6 <= a <= 20:
    print("Weird")

"""
Вариант 2, со вложенным if'ом:
if a % 2 != 0 and a > 20:
    print("Not Weird")
elif a % 2 != 0:
    print("Weird")
elif a % 2 == 0:
    if 2 <= a <= 5:
        print("Not Weird")
    if 6 <= a <= 20:
        print("Weird")
"""
