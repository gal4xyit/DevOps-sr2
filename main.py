from stringUtils import (
    print_text,
    print_case_info,
    get_uppercase_letters,
)
from generators import parity_generator


def main():
    print_text("Hello!")

    print_case_info("HELLO")
    print_case_info("hello")
    print_case_info("Hello")
    print_case_info("123!")

    letters = get_uppercase_letters("smogtether")
    print(letters)

    labels = parity_generator()

    for _ in range(6):
        print(next(labels))

    print("\nПеревірка неправильних аргументів:")

    try:
        print_text(123)
    except TypeError as error:
        print(f"Помилка: {error}")

    try:
        print_case_info(None)
    except TypeError as error:
        print(f"Помилка: {error}")

    try:
        get_uppercase_letters(["s", "m"])
    except TypeError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()