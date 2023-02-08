# This code is used for calculating Successive Multiplication

from mathCalculation.mathCalc import *

# Main function    
def main():
    while True:
        num1 = float(input('Enter the Base_x number: '))
        num2 = int(input('Enter the Radix number: '))
        print()

        if s_mult.basicMult(num1,num2) > 1:
            s_mult.greaterThanOne(num1,num2)
            
        elif s_mult.basicMult(num1,num2) < 1:
            s_mult.lessThanOne(num1,num2)

        elif s_mult.basicMult(num1,num2) == 1:
            s_mult.equalsOne(num1,num2)

main()
