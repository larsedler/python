# Beginning
character_name = "John"
character_age = "35"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")
print("he like the name " + character_name + ". ")
print("but didn't like being " + character_age + ".")

# Chaining of functions
phrase = "Giraffe Academy"
print(phrase.upper().isupper())
print(len(phrase))

# Using indices - first position in Python is 0
# "G"
print(phrase[0])
# "a"
print(phrase[3])

# Index function
print(phrase.index("a"))
print(phrase.index("Acad"))

# Replace function
print(phrase.replace("Giraffe", "Elephant"))

# Working with numbers
print(2)

# Modulus Operator - prints the remainer of the calculation
print(10 % 3)

my_num = 5
print(my_num)
print(str(my_num) + " my favorite number.")

my_num = -5
print(abs(my_num))

# "3" base to the power of "2"
print(pow(3, 2))

print(max(3, 2))
print(min(3, 2))
print(round(3.7))

# Importing code from packages/other code
from math import *

print(ceil(my_num))
print(floor(my_num))
print(sqrt(my_num))

# Getting input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old.")

# Basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result_str = num1 + num2  # turns out to be "45"
result_int = int(num1) + int(num2)  # no decimals allowed
result_flt = float(num1) + float(num2)  # decimals allowed
print(result_str)

# Mac Libs Game
print("Roses are red")
print("Violets are blue")
print("I love you")

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# Lists
friends = ["Kevin", "Karen", "Jim", "Oscar", "Theo"]
# friends = ["Kevin", 2.56, False]
friends[1] = "Mike"

print(friends)
print(friends[1])
print(friends[-1])  # indexing with negative values possible
print(friends[1:])  # "Karen" and everything after
print(friends[1:3])

lucky_numbers = [4, 8, 15, 16, 23, 42]
print(friends.extend(lucky_numbers))

# Tuples
# coordinates = (4, 5)    # inmutable -> cannot be changed or modified
coordinates = [(4, 5), (6, 7), (80, 34)]  # if you need to change something, use lists instead!!!
# coordinates[1] = 10     # won't work -> inmutable
print(coordinates[1])  # indexing starts always with 0


# Functions
# Code has to be indented in order to be recognized as functional code
def sayhi(name, age):
    print("Hello " + name + ", your are " + age + "!")


# print("Top")
sayhi("Lars", "43")


# print("Bottom")

# Return Statement
def cube(num):
    return num * num * num  # Statements after "return" will not gonna work!
    # "return" is considered to be the end of the function


result = cube(4)
print(result)

# If-Statements
is_male = False
is_tall = True

if is_male and is_tall:
    print("Your are a tall male!")
elif is_male and not (is_tall):
    print("You are a short male!")
elif not (is_male) and is_tall:
    print("You are a male but not tall!")
else:
    print("Your are not male and not tall!")


# if Statements & Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:  # also possible: e.g. "dog" == "dog" or != -> not equal to...
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 4, 5))

# Building a better calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator!")

# Dictionaries (curled braces)
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Mey": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Luv", "Not a valid key!"))
print(monthConversions.get("Aug", "Not a valid key!"))

# While-Loops
i = 1
while i <= 10:
    print(i)
    i = i + 1  # i += 1

print("Done with the loop.")

# Building a guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses! YOU LOSE!")
else:
    print("You win!")

# For-Loops
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
for index in range(3, 10):
    print(index)
for index in range(len(friends)):
    print(friends[index])
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")


# Exponent function
# print(2**3)       # easy approach

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 4))

# 2D Lists & Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8],
    [0]
]

print(number_grid[1][2])

for row in number_grid:
    for col in row:
        print(col)


# Build a translator
# Example:
# Giraffe  Language
# vowels -> g
# -----------
# dog -> dgg
# cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

# Try excepts
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError as err:
    print(err)

# Reading files

# first: open the file
employee_file = open("employees.txt", "r")

print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

# close the file
employee_file.close()

# Writing to files
# a - append; w - write
# create new file: just type in a new file name
employee_file = open("employees1.txt", "w")

employee_file.write("\nToby - Human Resources")

employee_file.close()

# Modules and Pip -> refers to file "useful_tools.py"
# Google: list of python modules (e.g. https://docs.python.org/3/py-modindex.html)
import useful_tools

print(useful_tools.roll_dice(10))

# Classes & Objects
# refers to class definiton "Student.py"
from Student import Student  # From file Student I want to import the class Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student2.gpa)

# Building a Multiple Choice Quiz
# refers to "Question.py"
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))


run_test(questions)

# Object Function
# refers to "Student.py"
from Student import Student

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, True)

print(student2.on_honor_roll())

# Inheritance
# refers to "Chef.py" and "ChineseChef.py"
from Chef import Chef

myChef = Chef()
myChef.make_special_dish()
