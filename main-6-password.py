
password = "sdfdsf23432\"DSFSDVFf"                           # input("Введiть пароль: ")

for char in password:
    dov = 1 if len(password) >= 8 else 0                        # dov - довжина паролю
    ts = 1 if any(char.isdigit() for char in password) else 0   # ts - наявнiсть цифр у паролi
    # при этом "ts = 1 if char.isdigit() else 0" даёт 0. И в таком случае зачем фор?
    v_b = 1 if password.isupper() else 0                        # v_b - велика буква
    m_b = 1 if password.islower() else 0                        # m_b - мала буква
    s_s = "`~!@#$%^&*()_-+={}[]\|:;\"'<>,.?/"                   # s_s - спецiальнi символи
    sym = 1 if any(char in s_s for char in password) else 0     # sym - наявнiсть спец. символiв
    sum = dov + ts + v_b + m_b + sym                            # Кiлькiсть набраних балiв
print(f"Мiцнiсть пароля: {sum} з 5!")
print(f"Длина {dov}, цифры {ts}, б. буквы {v_b}, м. буквы {m_b}, символы: {sym}")
