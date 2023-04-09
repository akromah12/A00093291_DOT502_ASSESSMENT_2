# This is a simple maths calculator

from multiplication import mutiply
from subtration import subtract
from division import division

def addition(a,b):
    return (a+b)

# This code allows a user to input numbers
if __name__ == "__main__":
    firstNumber = float(input("Please Enter first number: "))
    secondNumber = float(input("Please Enter second number: "))

    # The output of the two numbers
    print("The summation of the two numbers is:",addition(firstNumber,secondNumber))
    print("The subtraction of the two numbers is:",subtract(firstNumber,secondNumber))
    print("The multiplication of the two numbers is:",mutiply(firstNumber,secondNumber))
    print("The division of the two numbers is:",division(firstNumber,secondNumber))


    


