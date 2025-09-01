def has_digit(password):
    return any(letter.isdigit() for letter in password)


def is_very_long(password):
    return len(password) > 8


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def main():
    password = input("Введите пароль: ")
    score = 0
    checklist = [
        has_digit,
        is_very_long,
        has_lower_letters,
        has_upper_letters,
        has_symbols,
        ]

    for check in checklist:
        if check(password):
            score += 2

    print("Рейтинг пароля:", score)


if __name__ == '__main__':
    main()
