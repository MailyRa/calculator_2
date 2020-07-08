"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print("Welcome to Calculator")

#ask the user about the equation
def calculator_2():   

    user_input = (input(" Type your equation  "))

    num = user_input.split(' ')

#if the first letter is a "q" then I kno they want to quit 
    if num == ["q"]:
        print("Thank you, have a good day")

#the rest of the other functions 
    if num[0] == "+":
        return int(num[1]) + int(num[2])

    elif num[0] == "-":
        return int(num[1]) - int(num[2])

    elif num[0] == "*":
        return int(num[1]) * int(num[2])

    elif num[0] == "/":
        return int(num[1]) / int(num[2])

    elif num[0] == "square":
        return int(num[1]) * int(num[1])

    elif num[0] == "cube":
        return int(num[1]) * int(num[1]) * int(num[1]) 

    elif num[0] == "pow":
        return int(num[1]) ** int(num[2])

    elif num[0] == "mod":
        return int(num[1]) % int(num[2])
        

print(calculator_2())








