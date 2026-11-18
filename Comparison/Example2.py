number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
largest = number1
if largest < number2:
    largest = number2
if largest < number3:
    largest = number3
print("The largest number is", largest) 
