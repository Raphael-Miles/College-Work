def addition(x, y): 
        print(x + y)  # Function takes x and y. Can be any number, adds them together and prints the result

def subtraction(x, y):
        print(x - y)  # Function takes x and y. Can be any number, subtracts x from y and prints the result

def multiplication(x, y):
        print(x * y)  # Function takes x and y. Can be any number, multiplies the 2 numbers and prints the result

def division(x, y):
        print(x % y)  # Function takes x and y. Can be any number, divides y from x and prints the result


x = int(input('X = '))  # Asks for input to calculate
y = int(input('Y = '))

addition(x, y)  # Function runs
subtraction(x, y)
multiplication(x, y)
division(x, y)

