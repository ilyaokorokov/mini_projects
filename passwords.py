import random

# Константы символов
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous_chars = 'il1Lo0O'

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

# Считывание пользовательских данных
num_passwords = int(input("Введите количество паролей для генерации: "))
password_length = int(input("Введите длину пароля: "))

include_digits = input("Включать цифры (0123456789)? (да/нет): ").lower() == 'да'
include_lowercase = input("Включать строчные буквы (abcdefghijklmnopqrstuvwxyz)? (да/нет): ").lower() == 'да'
include_uppercase = input("Включать прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (да/нет): ").lower() == 'да'
include_punctuation = input("Включать символы !#$%&*+-=?@^_? (да/нет): ").lower() == 'да'
exclude_ambiguous = input("Исключать неоднозначные символы il1Lo0O? (да/нет): ").lower() == 'да'

# Формирование переменной chars на основе пользовательского ввода
chars = ''
if include_digits:
    chars += digits
if include_lowercase:
    chars += lowercase_letters
if include_uppercase:
    chars += uppercase_letters
if include_punctuation:
    chars += punctuation
if exclude_ambiguous:
    for char in ambiguous_chars:
        chars = chars.replace(char, '')

# Генерация паролей
print("\nСгенерированные пароли:")
for _ in range(num_passwords):
    password = generate_password(password_length, chars)
    print(password)
