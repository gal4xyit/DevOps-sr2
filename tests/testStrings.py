import unittest
from contextlib import redirect_stdout
from io import StringIO

from stringUtils import (
    print_text,
    print_case_info,
    get_uppercase_letters,
)


class TestStringUtils(unittest.TestCase):
    def test_print_text(self):
        output = StringIO()

        with redirect_stdout(output):
            print_text("Привіт!")

        self.assertEqual(output.getvalue(), "Привіт!\n")

    def test_case_info(self):
        cases = [
            ("HELLO", "Усі літери великі"),
            ("hello", "Усі літери малі"),
            ("Hello", "Регістр літер змішаний"),
            ("ПРИВІТ", "Усі літери великі"),
            ("привіт", "Усі літери малі"),
            ("Привіт", "Регістр літер змішаний"),
            ("HELLO 123", "Усі літери великі"),
            ("hello 123", "Усі літери малі"),
            ("123!", "У рядку немає літер із регістром"),
            ("", "У рядку немає літер із регістром"),
        ]

        for text, expected in cases:
            with self.subTest(text=text):
                output = StringIO()

                with redirect_stdout(output):
                    print_case_info(text)

                self.assertEqual(output.getvalue(), expected + "\n")

    def test_uppercase_letters(self):
        self.assertEqual(
            get_uppercase_letters("smogtether"),
            ["S", "M", "O", "G", "T", "E", "T", "H", "E", "R"],
        )

    def test_empty_uppercase_list(self):
        self.assertEqual(get_uppercase_letters(""), [])

    def test_rejects_non_strings(self):
        functions = (print_text, print_case_info, get_uppercase_letters)
        invalid_values = (123, 3.14, None, ["a"], True)

        for function in functions:
            for value in invalid_values:
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(TypeError):
                        function(value)

    def test_error_mentions_actual_type(self):
        with self.assertRaisesRegex(TypeError, "отримано int"):
            print_text(123)