# This feature allows the calculator to perform subtraction

def subtraction(a,b):
    return (a-b)
  
if __name__ == "__main__":
    firstNumber = float(input("Please Enter first number: "))
    secondNumber = float(input("Please Enter second number: "))

    # The output of the two numbers
    print("The subtraction of the two numbers is:" ,subtraction(firstNumber,secondNumber))
