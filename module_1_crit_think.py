



def addNumbers(num1, num2):
    return num1 + num2

def subtractNumbers(num1, num2):
    return num1 - num2

def multiplyNumbers(num1, num2):
    return num1 * num2

def divideNumbers(num1, num2):
    return num1 / num2


# Prints for user directions
print('\n### Please select calculation mode. ###\n')
print("Press 'A' for addition")
print("Press 'S' for subtraction")
print("Press 'M' for multiplication")
print("Press 'D' for division\n")

print("Press 'Q' to exit the program\n")

while True:
        
    # user picks calculation
    user_input = input('Select Mode: ')
    
    if user_input.lower() == 'q':
        break
    
    # check if valid character entered
    if user_input.lower() not in ['a', 's', 'd', 'm']:
        print('\n--- Unknown user input. Please try again. ---\n')
        continue
    
    # record user input of 2 numbers
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    
    # check if numbers inputted
    if not num1.isdigit() or not num2.isdigit():
        print('\n--- Both numbers must be positive whole numbers ---\n')
        continue
    
    # execute calculation
    if user_input.lower() == 'a':
        print("\n -- Result: ", addNumbers(int(num1), int(num2)))
    elif user_input.lower() == 's':
        print("\n -- Result: ", subtractNumbers(int(num1), int(num2)))
    elif user_input.lower() == 'm':
        print("\n -- Result: ", multiplyNumbers(int(num1), int(num2)))
    elif user_input.lower() == 'd':
        print("\n -- Result: ", divideNumbers(int(num1), int(num2)))
    
    print("\n")