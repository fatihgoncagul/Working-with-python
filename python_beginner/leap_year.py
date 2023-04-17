year = int(input("which year do you wanna check?\n"))

if year %4 == 0 and year % 100 !=0 :
    print("it is a leap year")
elif year % 4 ==0 and year % 100 ==0 and year % 400 ==0:
    print("it is a leap year")
else:
    print("it is not a leap year")

if year % 4 == 0:
    if year % 100 ==0:
        if  year % 400 ==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")