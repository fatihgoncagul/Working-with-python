print("Welcome to the tip calculator")
total = float(input("was the total bill?\n"))
tip_percentage = int(input("what percentage would you like to give"+
                           " 10, 12 or 15?\n"))
num_peoople = int(input("how many people to split the bill?\n"))
tip = round(total*(tip_percentage/100), 2)
total_and_tip = total + tip
each_bill = total_and_tip/num_peoople
each_bill = "{:.2f}".format(each_bill)
print(f"each personn should pay: {each_bill}")
