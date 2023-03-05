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
    def resultCheck(value):
        if value == 10:
            return 'A'
        elif value == 11:
            return 'B'
        elif value == 12:
            return 'C'
        elif value == 13:
            return 'D'
        elif value == 14:
            return 'E'
        elif value == 15:
            return 'F'
    def divRes(i,j):
        print('With the Integer Quotient ----> ', s_div.basicDiv(i,j))
        q_result = s_div.basicMod(i,j)
        if j == 16 and (9 < q_result < 16):
            value = s_div.resultCheck(q_result)
            print('The modulus of ', i, ' and ', j, ' is ----> ', value)
        else:
            print('The modulus of ', i, ' and ', j, ' is ----> ', q_result)
        print('---------------------------------------------------')
