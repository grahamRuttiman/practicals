
lower = 33
upper = 127

def get_number(lower, upper):
    try:
        number = int(input("Enter a number between {} and {}:".format(lower, upper)))
    except ValueError:
        print("Please entert a valid number")
    number = int(input("Enter a number between {} and {}:".format(lower, upper)))
    while number < lower or number > upper:
        return number = int(input("Enter a number between {} and {}:".format(lower, upper)))
get_number(lower,upper)

