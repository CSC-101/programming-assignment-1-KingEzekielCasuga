import math

import data
import hw1
import unittest

from data import Price, Rectangle, Employee, Point
from hw1 import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_area, books_by_author, circle_bound, \
    below_pay_average


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_vowel_count_1(self):
        input = 'Burger'
        result = vowel_count(input)
        expected = 2
        self.assertEqual(expected,result)

    def test_vowel_count_2(self):
        input = 'TEETHing'
        result = vowel_count(input)
        expected = 3
        self.assertEqual(expected,result)

    # Part 2

    def test_short_lists_1(self):
        input = [[3, 4, 7], [2, 2], [0], [6, 4], [44, 2, 3], [0, 3]]
        result = short_lists(input)
        expected = [[2, 2], [6, 4], [0, 3]]
        self.assertEqual(result, expected)

    def test_short_lists_2(self):
        input = [[3, 2, 4, 4, 4, 1 ,19, 0], [2, 0], [-7], [-7, 867], [3, 0, 3, 18], [4, 3]]
        result = short_lists(input)
        expected = [[2, 0], [-7, 867], [4, 3]]
        self.assertEqual(result, expected)

    # Part 3

    def test_ascending_pairs_1(self):
        input = [[3, 2, 4, 4, 4, 1 ,19, 0], [2, 0], [-7], [-7, 867], [3, 0, 3, 18], [4, 3]]
        result = ascending_pairs(input)
        expected = [[3, 2, 4, 4, 4, 1 ,19, 0], [0, 2], [-7], [-7, 867], [3, 0, 3, 18], [3, 4]]
        self.assertEqual(result, expected)

    def test_ascending_pairs_2(self):
        input = [[3, 4, 7], [2, 2], [0], [6, 4], [44, 2, 3], [0, 3]]
        result = ascending_pairs(input)
        expected = [[3, 4, 7], [2, 2], [0], [4, 6], [44, 2, 3], [0, 3]]
        self.assertEqual(result, expected)

    # Part 4

    def test_add_prices_1(self):
        input1 = Price(4, 87)
        input2 = Price(23, 55)
        result = add_prices(input1, input2)
        expected = Price(28, 42)
        self.assertEqual(result, expected)

    def test_add_prices_2(self):
        input1 = Price(0, 99)
        input2 = Price(0, 1)
        result = add_prices(input1, input2)
        expected = Price(1, 0)
        self.assertEqual(result, expected)

    # Part 5

    def test_rectangle_area_1(self):
        input = Rectangle(Point(0, 5), Point(10, 0))
        result = rectangle_area(input)
        expected = 50
        self.assertEqual(result, expected)

    def test_rectangle_area_2(self):
        input = Rectangle(Point(-20, 5), Point(20, 0))
        result = rectangle_area(input)
        expected = 200
        self.assertEqual(result, expected)

    # Part 6

    def test_books_by_author_1(self):
        input1 = 'Barack Obama'
        input2 = [data.Book(['My Friend bob', 'Barack Obama'], 'President\'s Guide'), data.Book(['R.L. Stein'], 'Goosebumps')]
        result = books_by_author(input1, input2)
        expected = ['President\'s Guide']
        self.assertEqual(result, expected)

    def test_books_by_author_2(self):
        input1 = 'R.L. Stein'
        input2 = [data.Book(['JK Rowling', 'Barack Obama'], 'Harry Potter'), data.Book(['R.L. Stein'], 'Goosebumps')]
        result = books_by_author(input1, input2)
        expected = ['Goosebumps']
        self.assertEqual(result, expected)

    # Part 7

    def test_circle_bound_1(self):
        input = Rectangle(data.Point(1, 1), data.Point(5, -1))
        result = circle_bound(input)
        expected = data.Circle(data.Point(3,0), math.sqrt(5))
        self.assertEqual(result, expected)

    def test_circle_bound_2(self):
        input = Rectangle(data.Point(0, 5), data.Point(-4, 1))
        result = circle_bound(input)
        expected = data.Circle(data.Point(-2,3), 2*math.sqrt(2))
        self.assertEqual(result, expected)

    # Part 8

    def test_below_pay_average_1(self):
        input = [Employee('Janet', 15), Employee('Sharon', 26), Employee('Michael', 20)]
        result = below_pay_average(input)
        expected = ['Janet', 'Michael']
        self.assertEqual(result, expected)

    def test_below_pay_average_2(self):
        input = [Employee('Charlie', 0), Employee('Bailey', 26), Employee('Eli', 1)]
        result = below_pay_average(input)
        expected = ['Charlie', 'Eli']
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
