# This file conatains calculation methods for multiple files

class s_mult:
    def basicMult(x,y):
        mult = x * y
        return mult
    def greaterThanOne(i,j):
        tempProduct = s_mult.basicMult(i,j)
        numRem = tempProduct - 1
        numInt = tempProduct - numRem
        print('With the Integer Quotient ----> ', numInt)
        print('The remainder of ', i, ' and ', j, ' is ----> ', round(numRem,2))
        print('---------------------------------------------------')
    def lessThanOne(i,j):
        tempProduct = s_mult.basicMult(i,j)
        noInt = 0
        print('With the Integer Quotient ----> ', noInt)
        print('The remainder of ', i, ' and ', j, ' is ----> ', round(tempProduct,2))
        print('---------------------------------------------------')
    def equalsOne(i,j):
        tempProduct = s_mult.basicMult(i,j)
        noRem = 0
        print('With the Integer Quotient ----> ', tempProduct)
        print('The remainder of ', i, ' and ', j, ' is ----> ', round(noRem,2))
        print('---------------------------------------------------')

class s_div:
    def basicMod(i,j):
        modRes = i % j
        return modRes
    def tempVal(i,j):
        modNum = s_div.basicMod(i,j)
        tempNum = i - modNum
        return tempNum
    def basicDiv(i,j):
        tempNum = s_div.tempVal(i,j)
        numDiv = tempNum // j
        return numDiv
    def divRes(i,j):
        print('With the Integer Quotient ----> ', s_div.basicDiv(i,j))
        print('The modulus of ', i, ' and ', j, ' is ----> ', s_div.basicMod(i,j))
        print('---------------------------------------------------')
