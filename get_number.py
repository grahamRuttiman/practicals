
lower = 33
upper = 127
def get_number(lower, upper):
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
    return True
get_number(lower,upper)

