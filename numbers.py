import random

def is_valid(input_str):
    """Проверяет, является ли введенная строка целым числом от 1 до 100."""
    if input_str.isdigit():
        num = int(input_str)
        return 1 <= num <= 100
    return False

def guess_number_game():
    print("Добро пожаловать в числовую угадайку")

    while True:
        upper_bound = input("Введите правую границу для случайного выбора числа (от 1 до n): ")
        if upper_bound.isdigit() and int(upper_bound) >= 1:
            upper_bound = int(upper_bound)
            break
        else:
            print("А может быть все-таки введем целое число больше 0?")

    secret_number = random.randint(1, upper_bound)
    attempts = 0

    while True:
        user_input = input(f"Угадайте число от 1 до {upper_bound}: ")
        
        if not is_valid(user_input):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif guess > secret_number:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print(f"Вы угадали, поздравляем! Количество попыток: {attempts}")
            break

    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

    while True:
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again in ('да', 'нет'):
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

    if play_again == 'да':
        guess_number_game()
    else:
        print("До свидания!")

# Запуск игры
guess_number_game()
