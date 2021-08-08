#Defining main functions of calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

print("Select operation:\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Modulo\n"
      )

#Receive user input + Error handling for option selection
while True:
    try:
        selectOption = int(input("Select option: "))
        if selectOption < 1 or selectOption > 5:
            print("Please enter a valid integer!")
        else:
            break
    except ValueError:
        print("Please enter an integer!")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if selectOption == 1:
    print("Answer = ", add(number1, number2))

if selectOption == 2:
    print("Answer = ", subtract(number1, number2))

if selectOption == 3:
    print("Answer = ", multiply(number1, number2))

if selectOption == 4:
    print("Answer = ", divide(number1, number2))

if selectOption == 5:
    print("Answer = ", modulo(number1, number2))
