# *args : many positional arguments
def add(*args):
    sum = 0
    print(args)  # args is gonna be a tuple
    for n in args:
        print(n)
        sum += n
    return sum


print(f"sum : {add(3, 5, 6, 4, 5)}")

# **kwargs : arbitrary number of keyword arguments
# lets us look through and find the ones we want
# and use them to the something
print("*********************")


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=3)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"] #if user does not give when we wrote this in square bracket it gives error
        self.model = kw.get("model") # so we use get method it doesnt give error returns none if user doesnt use this


my_car = Car(make= "nissan")
print(my_car.make)
print(my_car.model)


