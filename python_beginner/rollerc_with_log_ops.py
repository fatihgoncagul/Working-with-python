print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0;
if height >= 120:
    print("u can ride rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5;
        print("child tickets $5")
    elif age <= 18:
        bill = 7;
        print("youth tickets $7")
    elif 45 <= age <= 55:
        print("Everything is gonna be ok. have a free ride on us")
    else:
        bill = 12;
        print("adult tickets are $12")
    wants_photo =input("do you want a photo taken? Y or N\n")
    if wants_photo == "Y":
        bill += 3

    print(f"Your bill is ${bill} dollars.")

else:
    print("sorry grew up")
# we are gonna add midlife crisis free tickets
# 45-55 age : free ticket

