# write a program that shows how many
# days weeks and months left if you lived til 90 years
age = int(input("whats your current age\n"))
years_left = 90-age
weeks = years_left*52
months = years_left*12
days = years_left*365
print(f"You have {days}, {weeks} weeks, and {months} months left")