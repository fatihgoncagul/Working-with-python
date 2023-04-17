def greet():
    print("hello")
    print("how do you do?")
    print("is not the weather nice today?")


greet()

#  function that allows for input
print("----------with a parameter")


def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do you do {name}?")
    print(f"is not the weather nice today?")


greet_with_name("Angela")

print("----------multiple parameters")


def greet_with(name, location):
    print(f"hello {name}")
    print(f"how is the weather in {location}")


greet_with("fatih", "antalya")
greet_with(location="london", name="angela")


