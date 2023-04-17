height = float(input("whats your height in m?\n"))
weight = float(input("whats your weight in kg?\n"))

bmi = int(weight/height**2)
print("your bmi is "+ str(bmi))

# rounding numbers

print(round(8/3))
print(round(8/3, 2))  # 2 decimal places
print(8//3)  # floor division, gives us an int
print(8 % 3)  # 8 mod 3 = 2
result = 4/2
result /= 2
result += 1
result -= 1
# f strings
print("your score is "+ str(result))
score = 0
heigt_2 = 1.8
isWinning = True
print(f"your score is [{score}, your height is {heigt_2},"
      f" you are winning is {isWinning}")

