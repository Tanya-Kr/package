import unittest
from unittest import TestCase, main, TestSuite
from package.task10 import calculation


class AddTest(TestCase):

    def test_all_args_more_zero(self):
        num1 = 3
        num2 = 5
        expected = 8

        actual = calculation.add(num1, num2)

        self.assertEqual(expected, actual)

    def test_all_args_less_zero(self):
        num1 = -3
        num2 = -5
        expected = -8

        actual = calculation.add(num1, num2)

        self.assertEqual(expected, actual)

    def test_one_arg_less_zero(self):
        num1 = 3
        num2 = -5
        expected = -2

        actual = calculation.add(num1, num2)

        self.assertEqual(expected, actual)


class SubtractTest(TestCase):
    def test_all_args_more_zero(self):
        num1 = 3
        num2 = 5
        expected = -2

        actual = calculation.subtract(num1, num2)

        self.assertEqual(expected, actual)

    def test_all_args_less_zero(self):
        num1 = -3
        num2 = -5
        expected = 2

        actual = calculation.subtract(num1, num2)

        self.assertEqual(expected, actual)

    def test_one_arg_less_zero(self):
        num1 = 3
        num2 = -5
        expected = 8

        actual = calculation.subtract(num1, num2)

        self.assertEqual(expected, actual)


def suite_one_arg_less_zero():
    suite = unittest.TestSuite()
    suite.addTest(AddTest.test_one_arg_less_zero)
    suite.addTest(SubtractTest.test_one_arg_less_zero)
    return suite


def suite_all_args_more_zero():
    suite = unittest.TestSuite()
    suite.addTest(AddTest.test_all_args_more_zero)
    suite.addTest(SubtractTest.test_all_args_more_zero)
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite_one_arg_less_zero())
    unittest.TextTestRunner().run(suite_all_args_more_zero())