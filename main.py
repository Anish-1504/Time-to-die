#  calculating days, months & years left to live - taking max age 90
age = input("What is your current age?\n ")

age1 = int(age)
years = 90 - age1
days = years*365
weeks = years*52
months =  years*12

print(f"You have {days} days, {weeks} weeks, and {months} months left. ")


