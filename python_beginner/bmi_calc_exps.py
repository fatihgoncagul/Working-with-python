height = float(input("whats your height in m?\n"))
weight = float(input("whats your weight in kg?\n"))

bmi = int(weight/height**2)
print("your bmi is "+ str(bmi))

if bmi < 18.5:
    print("you are underweight eat a little more")
elif bmi < 25 :
    print("congrats you have normal weight")
elif bmi < 30:
    print("you are kind of an overweight dude")
elif bmi < 35:
    print("obese")
else:
    print("you are clinically obese go see a doc")