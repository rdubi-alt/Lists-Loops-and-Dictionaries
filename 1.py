#variables
day = 20
#only prints when you say print
print (day)

#math with int and float
print(day * 3)
calories = 99.7
cups = 2

#strings
movie = "Watership Down"
#when you want to use single/double quotes within a string, use \
store = 'Nick\'s Pizza Shop, the "best" there is'

#string + variables: use f"[] {variable} []"
day = 25
day_name = "Monday"
month = "October"
temp = 65

print(f"Today is {day_name}, {month} {day} and it's {temp} degrees outside.")

#Boolian-can be either True or False
glass_is_full = False

if glass_is_full:
    print("Drink up!")
#make something else happen if boolian statement is False
else:
    print("Drought...")

age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You're but a wee child.")
