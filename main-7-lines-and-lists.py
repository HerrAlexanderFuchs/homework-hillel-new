
print("Завдання №1")
wort = input("Введiть слово: ")
if wort == wort[::-1]:
    print("+\n")
else:
    print("-\n")

print("Завдання №2")
linie = input("Введiть строку: ")
teil = input("Введiть текст для пошуку у строцi: ")
if linie.count(teil) == 1:
    print("YES\n")
else:
    print("NO\n")

print("Завдання №3")
linie = input("Введiть строку: ")
if linie.startswith("abc"):
    print(linie.replace("abc", "www"))
    print()
else:
    print(linie + "qqq\n")

print("Завдання №4")
linie = input("Введiть строку: ")
ergebnis = ""                           # Результат
for char in linie:
    if not char.isdigit():              # перевірка, чи символ цифорою
        ergebnis += char                # додаємо символ у змінну "результат"
print(f"Результат: {ergebnis}\n")

print("Завдання №5")
e_mail = input("Введiть електронну пошту: ")
if e_mail.count("@") == 1 and e_mail.count(".") == 1:
    print("YES")
else:
    print("NO")
