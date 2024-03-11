import random
import string
def generate_password(letters=True, symbols=False, numbers=False, duplicates=False, pass_length=8):
    #довжина паролю не менша за 8 символів
    if pass_length < 8:
        print("Пароль має містити принаймні 8 символів")
        return

    charset = ""  # Рядок з символами для генерації паролю
    password = ""  # Змінна з генерованим паролема

    # Додавання символів в залежності від вказаних параметрів
    if letters:
        charset += string.ascii_letters  # Додаємо літери верхнього та нижнього регістру
    if symbols:
        charset += "!@#$%^&*()+"
    if numbers:
        charset += string.digits  # Додаємо цифри

    # Видаляємо повтори символів, якщо duplicates=False
    if not duplicates:
        charset = list(set(charset))

    # Якщо не було додано жодного символу, виводимо повідомлення та завершуємо функцію
    if len(charset) == 0:
        print("Немає символів для генерації паролю")
        return

    # Генерація паролю заданої довжини
    for i in range(pass_length):
        password += random.choice(charset)

    return password

print(generate_password()) 
print(generate_password(pass_length=6)) 
print(generate_password(letters=True, symbols=True, numbers=True, duplicates=True, pass_length=12))  