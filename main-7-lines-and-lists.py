
# print("Завдання №1")
# wort = input("Введiть слово: ")
# print("+" if wort == wort[::-1] else "-")
# print()
#
# print("Завдання №2")
# linie = input("Введiть строку: ")
# teil = input("Введiть текст для пошуку у строцi: ")
# print("YES" if linie.find(teil) else "NO")
# print()
#
# print("Завдання №3")
# linie = input("Введiть строку: ")
# print(linie.replace("abc", "www") if linie.startswith("abc") else linie + "qqq")
# print()

print("Завдання №4")
linie = list(input("Введiть строку: "))
neue_zeile = []                                # Создаём новую переменную с уже перебранной строкой (без цифр)
for char in linie:
    if not char.isdigit() or char.isspace():
        neue_zeile.append(char)
neue_zeile = "".join(neue_zeile).strip()       # "" - это разделение между элементами списка, стрипом удаляем пробелы
print(neue_zeile)