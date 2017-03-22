

#lower = 33
#upper = 127
#function for asking for a number between two limits122

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
    return number
#get_number(number,lower,upper)
#min_number = 33
#max_number = 127
#number = int(input("Enter a number between {} and {}:".format(min_number,max_number)))
#while number < min_number or number > max_number:
#    print("The number must be BETWEEN {} and {}".format(min_number, max_number))
#    number = int(input("Enter a number between {} and {}:".format(min_number, max_number)))
character = input("Enter a character:")
print("The ASCII code for",character,"is",ord(character))
num = get_number(33,127)
print (num)
print("The character for {} is {}".format(num), chr(num))
for i in range(lower,upper,1):
    print(" {} {: >6}".format(i,chr(i)))

#    print (i)
#    print (chr(i))
