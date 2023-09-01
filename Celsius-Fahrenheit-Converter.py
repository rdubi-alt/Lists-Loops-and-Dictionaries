# convert celsius to fahrenheit or vice versa

def temp_convert():
    temp_type = input("Celcius to Fahrenheit [1] or Fahrenheit to Celcius [2]? ")
    #try and except prevents errors if user doesn't input numbers
    try:
        if temp_type == "1":
            c = input("Celsius: ")
            c = float(c)
            f = c * 1.8 + 32
            print("Fahrenheit" , f)
        elif temp_type == "2":
            f = input("Fahrenheit: ")
            f = float(f)
            c = 5/9 * (f - 32)
            print("Celcius" , c)
        else:
            print("Please type either 1 or 2.")
            temp_convert()
    except:
        print("Please type a number.")
        temp_convert()

temp_convert()




