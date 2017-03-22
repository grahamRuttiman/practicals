
character = input("Enter a character:")
print("The ASCII code for",character,"is",ord(character))
lower = 33
upper = 127
#min_number = 33
#max_number = 127
#number = int(input("Enter a number between {} and {}:".format(min_number,max_number)))
#while number < min_number or number > max_number:
#    print("The number must be BETWEEN {} and {}".format(min_number, max_number))
#    number = int(input("Enter a number between {} and {}:".format(min_number, max_number)))
print("The character for {} is {}".format(number, chr(number)))
for i in range(lower,upper,1):
    print(" {} {: >6}".format(i,chr(i)))

#    print (i)
#    print (chr(i))
