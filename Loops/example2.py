# This program counts the number of odd and even numbers
# entered by the user until they enter 0 to stop.
odd_num = 0
even_num = 0
 

number = int(input("Enter a number or type 0 to stop: "))
 

while number != 0:
    
    if number % 2 == 1:
    
        odd_num += 1
    else:

        even_num += 1

    number = int(input("Enter a number or type 0 to stop: "))
 

print("Odd numbers count:", odd_num)
print("Even numbers count:", even_num)
 