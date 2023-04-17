# high order functions, passing function with parameter
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def calculator(n1, n2, func):
    func(n1, n2)


result = calculator(2, 3, subtract())

print(result)

# object state and instances

from turtle import Turtle

timmy = Turtle()
tommy = Turtle()
timmy.color("green")
tommy.color("purple")
# their state (nitelik) are different

