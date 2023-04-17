# prime number checker
# Write your code below this line 👇


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")


prime_checker(number=n)
