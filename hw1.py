from data import Price, Rectangle, Book, Circle, Point, Employee
import math


# Write your functions for each part in the space below.

# Part 1

# Takes in a word and returns the number of vowels in that word

def vowel_count(word:str) -> int:
    count = 0
    for letter in list(word):
        if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count = count + 1
    return count

# Part 2

# takes in a list of a list of numbers, and returns a list of those that were of length 2

def short_lists(outlist:list[list[int]]) -> list:
    short_list = []
    for inlist in outlist:
        if len(inlist) == 2:
            short_list.append(inlist)
    return short_list

# Part 3

# Takes in a list of integer lists, and returns the same list but
# those with length two are returned in ascending order

def ascending_pairs(netlist:list[list[int]]) -> list:
    ascend_list = []
    for list in netlist:
        if len(list) == 2 and list[0] > list[1]:
            ascend_list.append(list[::-1])
        else:
            ascend_list.append(list)
    return ascend_list

# Part 4

# Adds two prices together, and if the cents reach over 99 then it rolls over into the dollars

def add_prices(price1:Price, price2:Price):
    cents_total = Price(0, price1.cents + price2.cents)
    if cents_total.cents > 99:
        cents_total.cents = cents_total.cents - 100
        cents_total.dollars = 1
    new_price = Price(price1.dollars + price2.dollars + cents_total.dollars, cents_total.cents)
    return new_price

# Part 5

# Takes in a rectangle and returns its area

def rectangle_area(rectangle:Rectangle):
    return abs(rectangle.top_left.x-rectangle.bottom_right.x) * abs(rectangle.top_left.y-rectangle.bottom_right.y)

# Part 6

# takes a list of books and an author and returns a list of books written by that author

def books_by_author(author_name:str, books:list[Book]) -> list:
    book_list = []
    for book in books:
        for author in book.authors:
            if author_name == author:
                book_list.append(book.title)
    return book_list

# Part 7

# Takes in a rectangle and returns a bounding circle where only the corners of the rectangle make contact

def circle_bound(rectangle:Rectangle) -> Circle:
    hypotenuse = math.sqrt(((rectangle.top_left.x-rectangle.bottom_right.x) ** 2) + ((rectangle.top_left.y-rectangle.bottom_right.y) ** 2))
    bound_radius = (hypotenuse/2)
    bound_center = Point((rectangle.top_left.x+rectangle.bottom_right.x)/2, (rectangle.top_left.y+rectangle.bottom_right.y)/2)
    bounding_circle = Circle(bound_center,bound_radius)
    return bounding_circle

# Part 8

# Takes in a list of employees and returns the employee names who are paid below the average of the list

def below_pay_average(employees:list[Employee]) -> list[str]:
    total_pay = 0
    for employee in employees:
        total_pay = total_pay + employee.pay_rate
    avg_pay = total_pay/len(employees)
    underpaid = []
    for employee in employees:
        if employee.pay_rate < avg_pay:
            underpaid.append(employee.name)
    return underpaid























