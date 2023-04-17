print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("u can ride rollercoaster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        print("please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("sorry grew up")
