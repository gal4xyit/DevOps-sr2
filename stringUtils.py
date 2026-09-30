def _validate_text(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент має бути рядком")


def print_text(text):
    _validate_text(text)
    print(text)


def print_case_info(text):
    _validate_text(text)

    if text.isupper():
        print("Усі літери великі")
    elif text.islower():
        print("Усі літери малі")
    elif text.lower() != text.upper():
        print("Регістр літер змішаний")
    else:
        print("У рядку немає літер із регістром")


def get_uppercase_letters(text):
    _validate_text(text)
    return list(map(lambda letter: letter.upper(), text))