def caesar_cipher(text, shift, alphabet):
    shifted_text = ''
    for char in text:
        if char.isalpha():  # проверяем, является ли символ буквой
            is_upper = char.isupper()  # сохраняем регистр символа
            char = char.lower()  # переводим в нижний регистр для работы с алфавитом
            index = (alphabet.index(char) + shift) % len(alphabet)  # находим новую позицию символа
            new_char = alphabet[index]  # получаем новый символ
            if is_upper:
                new_char = new_char.upper()  # восстанавливаем регистр, если был верхний
            shifted_text += new_char
        else:
            shifted_text += char  # символы не входящие в алфавит остаются без изменений
    return shifted_text

def main():
    direction = input("Выберите направление (шифрование или дешифрование): ").lower()
    language = input("Выберите язык алфавита (русский или английский): ").lower()
    shift = int(input("Введите шаг сдвига (целое число): "))
    text = input("Введите текст для обработки: ")

    if language == 'русский':
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    elif language == 'английский':
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    else:
        print("Неподдерживаемый язык алфавита. Выберите русский или английский.")
        return

    if direction == 'шифрование':
        result = caesar_cipher(text, shift, alphabet)
    elif direction == 'дешифрование':
        # Для дешифрования используем отрицательный шаг
        result = caesar_cipher(text, -shift, alphabet)
    else:
        print("Неправильное направление. Выберите 'шифрование' или 'дешифрование'.")
        return

    print("Результат обработки:")
    print(result)

if __name__ == "__main__":
    main()
