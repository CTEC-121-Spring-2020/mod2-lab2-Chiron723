"""
CTEC 121
<Stephen Guild>
<Mod 2 Lab 2>
<assignment/lab description>
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
#from math import *
import math
def main():
    """
    mystring ="Hello"
    print(mystring)
    print(type(mystring))
    myint=33
    print(myint)
    print(type(myint))

    r=3
    v=(4/3)*pi*r**3
    print("v",v)

    print("demo from input() page")
    # Get a string
    aString = input("Enter a string of characters: ")
    print(aString)

    # Print 2 blank lines
    # print("\n\n")

    # Get an integer
    #int(does not accept decimals or non-numeric)
    myInt = int(input("Enter a number: "))
    print(myInt)

    # Print 2 blank lines
    # print("\n\n")

    # Get a floating point number
    myFloat = float(input("Enter a number (decimals are ok): "))
    print(myFloat)

    # Print 2 blank lines
    # print("\n\n")

    # Evaluate an expression entered
    # Enter 3+4
    aNumber = eval(input("Enter a number or a numeric expressions: "))
    print(aNumber)

    # Print 2 blank lines
    # print("\n\n")

    

    x, y = eval(input("Enter two numbers separated by a comma: "))
    print(x, y)
    print(type(x))
    print()

    x, y = input("provide two values: ").split()
    print(x, y)
    print(type(x))
    x=int(x)
    print(type(x))
    print()
    
    #demo definite loops
    for i in [10, 1, 2, 3]:
        print(i)
    print()

    for count in range(4):
        print(count)
    print()

    for i in range(2,11,2):
        print(i)
    

    print(math.pi)
    print(math.sqrt(4))
    print(math.ceil(math.pi))
    print()

    sum = 0
    for i in [56, 19, 92, 67]:
        print(i)
        sum = sum + i
    print("----")
    print(sum)
    """

    sum = 0
    for i in range(5):
        inputValue=eval(input("input a value:"))
        sum=sum+inputValue
    print("sum", sum)
    print()









main()    