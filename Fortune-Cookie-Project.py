#you can make anything random by importing a python module-google "python random" to see all possible modules
import random
#Generates random "lucky number"
lucky_number = random.randint(1,100)
#Generates random integer between 1 and 3 
fortune_number = random.randint(1,3)
fortune_text = ""

#based on random fortune number, person will get their fortune told
if fortune_number == 1:
    fortune_text = "You will have a great day!"
if fortune_number == 2:
    fortune_text = "Today will be tough...but worth it."
if fortune_number == 3:
    fortune_text = "You will get married this year."

print(f"{fortune_text} Your Lucky Number is: {lucky_number}")
