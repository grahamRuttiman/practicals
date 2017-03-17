try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:
 print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
 print("Cannot divide by zero!")
print("Finished.")
# QUESTIONS:
# 1. A ValueError occurs when the value entered is not an integer, or even a number
# 2. A ZeroDivisionError occurs when the value of demoninator entered is zero
# 3. Before the fraction value is calculated we could use an if statement to print an error message if the demoninator value entered is zero