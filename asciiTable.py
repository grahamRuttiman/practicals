def get_number(lower, upper):
    """"Function to input number within upper and lower limits"""
    valid_number = False
    while valid_number == False:
        try:
           number = int(input("Enter a number between {} and {}:".format(lower, upper)))
        except ValueError:
           print("Please enter a valid number")
           number = int(input("Enter a number between {} and {}:".format(lower, upper)))

        while number < lower or number > upper:
            print("The number must be BETWEEN {} and {}".format(lower, upper))
            try:
                number = int(input("Enter a number between {} and {}:".format(lower, upper)))
            except ValueError:
                print("Please enter a valid number")
                number = int(input("Enter a number between {} and {}:".format(lower, upper)))
        else:
            valid_number = True
    return number

character = input("Enter a character:")
print("The ASCII code for",character,"is",ord(character))
num = get_number(33,127)
print("The character for {} is {}".format(num, chr(num)))
