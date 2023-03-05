## Introduction:
The following will demonstrate how to interpret the results produced by the program. Several examples have been provided converting Decimal to Binary, Octal, and Hexadecimal.

### What to know:
When running the program, the user will be prompted with a *Base_x* value and *Radix* value: 
- The *Base_x* value is the initial starting Decimal value that is going to be converted
- The *Radix* value is the new number representation base that the *Base_x* value is being converted to.

## Example run of the program:
```
$ python3 Successive_Division.py
Enter the Base_x number: 79
Enter the Radix number: 2

With the Integer Quotient ---->  39
The modulus of  79  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 39
Enter the Radix number: 2

With the Integer Quotient ---->  19
The modulus of  39  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 19
Enter the Radix number: 2

With the Integer Quotient ---->  9
The modulus of  19  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 9
Enter the Radix number: 2

With the Integer Quotient ---->  4
The modulus of  9  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 4
Enter the Radix number: 2

With the Integer Quotient ---->  2
The modulus of  4  and  2  is ---->  0
---------------------------------------------------
Enter the Base_x number: 2
Enter the Radix number: 2

With the Integer Quotient ---->  1
The modulus of  2  and  2  is ---->  0
---------------------------------------------------
Enter the Base_x number: 1
Enter the Radix number: 2

With the Integer Quotient ---->  0
The modulus of  1  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 
```
### Interpretation of the example run:
- In the example shown, the user is prompted with a *Base_x* value and *Radix* value. In the following example, the *Base_x* value that was chosen was **79** and the *Radix* is **2**. The interpretation of this is that we are converting the decimal (base 10) value of 79 the binary representation using base 2 (Radix value).
- Each run of the program will produce an *'Integer Quotient'* value and a *modulus* value. 
    - The *'Integer Quotient'* value is the value that will be used as the new *Base_x* value until it has reached zero. 
    - The *modulus* value is used to write the new base representation of our original *Base_x* value. In this case, it will a part of the representation of our new Binary representation of 79 (Because it is Binary, it is either a 1 or 0).
- After reaching an *'Integer Quotient'* value of zero, the *modulus* values will be read from bottom (Most Significant Bit) to top (Lease Significant Bit). In the example case, it will be read as the following:
    - 1001111
    - The following result shown, demonstrates the Binary representation of the original Decimal value 79.

## Example run of the program to convert Decimal to Binary:
```
$ python3 Successive_Division.py
Enter the Base_x number: 326
Enter the Radix number: 2

With the Integer Quotient ---->  163
The modulus of  326  and  2  is ---->  0
---------------------------------------------------
Enter the Base_x number: 163
Enter the Radix number: 2

With the Integer Quotient ---->  81
The modulus of  163  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 81
Enter the Radix number: 2

With the Integer Quotient ---->  40
The modulus of  81  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 40
Enter the Radix number: 2

With the Integer Quotient ---->  20
The modulus of  40  and  2  is ---->  0
---------------------------------------------------
Enter the Base_x number: 20
Enter the Radix number: 2

With the Integer Quotient ---->  10
The modulus of  20  and  2  is ---->  0
---------------------------------------------------
Enter the Base_x number: 10
Enter the Radix number: 2

With the Integer Quotient ---->  5
The modulus of  10  and  2  is ---->  0
---------------------------------------------------
Enter the Base_x number: 5
Enter the Radix number: 2

With the Integer Quotient ---->  2
The modulus of  5  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number: 2
Enter the Radix number: 2

With the Integer Quotient ---->  1
The modulus of  2  and  2  is ---->  0
---------------------------------------------------
Enter the Base_x number: 1
Enter the Radix number: 2

With the Integer Quotient ---->  0
The modulus of  1  and  2  is ---->  1
---------------------------------------------------
Enter the Base_x number:
```
### Input:
- Decimal value (Base 10): 326
- Radix value (Base 2): 2
### Result Interpretation:
- 101000110

## Example run of the program to convert Decimal to Octal:
```
$ python3 Successive_Division.py
Enter the Base_x number: 254
Enter the Radix number: 8

With the Integer Quotient ---->  31
The modulus of  254  and  8  is ---->  6
---------------------------------------------------
Enter the Base_x number: 31
Enter the Radix number: 8

With the Integer Quotient ---->  3
The modulus of  31  and  8  is ---->  7
---------------------------------------------------
Enter the Base_x number: 3
Enter the Radix number: 8

With the Integer Quotient ---->  0
The modulus of  3  and  8  is ---->  3
---------------------------------------------------
Enter the Base_x number:
```
### Input:
- Decimal value (Base 10): 256
- Radix value (Base 8): 8
### Result Interpretation:
- 376

## Example run of the program to convert Decimal to Hexadecimal:
```
$ python3 Successive_Division.py
Enter the Base_x number: 479
Enter the Radix number: 16

With the Integer Quotient ---->  29
The modulus of  479  and  16  is ---->  F
---------------------------------------------------
Enter the Base_x number: 29
Enter the Radix number: 16

With the Integer Quotient ---->  1
The modulus of  29  and  16  is ---->  D
---------------------------------------------------
Enter the Base_x number: 1
Enter the Radix number: 16

With the Integer Quotient ---->  0
The modulus of  1  and  16  is ---->  1
---------------------------------------------------
Enter the Base_x number:
```
### Input:
- Decimal value (Base 10): 479
- Radix value (Base 16): 16
### Result Interpretation:
- 1DF
