#make stuff random using python module-google python random to see all
#python random modules
import random
answer = random.randint(1,3)

if answer == 1:
    print("Yes")
if answer == 2:
    print("No")
if answer == 3:
    print("Maybe")

import random

lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)
fortune_text = ""

if fortune_number == 1:
    fortune_text = "You will have a great day!"
if fortune_number == 2:
    fortune_text = "Today will be tough...but worth it."
if fortune_number == 3:
    fortune_text = "You will get married this year."

print(f"{fortune_text} Your Lucky Number is: {lucky_number}")
