import unittest

from generators import parity_generator


class TestParityGenerator(unittest.TestCase):
    def test_first_value(self):
        generator = parity_generator()
        self.assertEqual(next(generator), "Парне")

    def test_alternates(self):
        generator = parity_generator()
        actual = [next(generator) for _ in range(100)]
        expected = ["Парне", "Непарне"] * 50

        self.assertEqual(actual, expected)

    def test_generators_are_independent(self):
        first = parity_generator()
        second = parity_generator()

        self.assertEqual(next(first), "Парне")
        self.assertEqual(next(second), "Парне")
        self.assertEqual(next(first), "Непарне")