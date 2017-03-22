
lower = 33
upper = 127

def get_number(lower, upper):
    try:
        number = int(input("Enter a number between {} and {}:".format(lower, upper)))
    except ValueError:
        print("Please entert a valid number")
    number = int(input("Enter a number between {} and {}:".format(lower, upper)))
    while number < lower or number > upper:
        print ("The number must be BETWEEN {} and {}".format(lower, upper)))
        return number = int(input("Enter a number between {} and {}:".format(lower, upper)))
    return True
get_number(lower,upper)

