
password = "sdfdsf23432@DSFSDVFf"               # input("Введiть пароль: ")

dov = 1 if len(password) >= 8 else 0            # dov - довжина паролю
ts = 1 if password.isdigit() else 0             # ts - наявнiсть цифр у паролi
v_b = 1 if password.isupper() else 0            # v_b - велика буква
m_b = 1 if password.islower() else 0            # m_b - мала буква
s_s = "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"       # s_s - спецiальнi символи
sym = 1 if any(char in s_s for char in password) else 0
sum = dov + ts + v_b + m_b + sym            # Кiлькiсть набраних балiв
print(f"Мiцнiсть пароля: {sum} з 5!")
print(f"Длина {dov}, цифры {ts}, б. буквы {v_b}, м. буквы {m_b}, символы: {sym}")