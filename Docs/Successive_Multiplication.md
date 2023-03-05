## Introduction:
The following will demonstrate how to interpret the results produced by the program. An example has been provided converting decimal value of Decimal representation of a number to Binary representation.

### What to know:
- When running the program, the user will be prompted with a *Base_x* value and *Radix* value: 
    - The *Base_x* value is the initial starting Decimal value that is going to be converted.
    - The *Radix* value is the new number representation base that the *Base_x* value is being converted to.
- This program is only used to convert decimal values for numbers in Decimal representation.

## Example run of the program:
```
$ python3 Successive_Multiplication.py
Enter the Base_x number: 0.35
Enter the Radix number: 2

With the Product whole value ---->  0
The remainder of  0.35  and  2  is ---->  0.7
---------------------------------------------------
Enter the Base_x number: 0.7
Enter the Radix number: 2

With the Product whole value ---->  1.0
The remainder of  0.7  and  2  is ---->  0.4
---------------------------------------------------
Enter the Base_x number: 0.4
Enter the Radix number: 2

With the Product whole value ---->  0
The remainder of  0.4  and  2  is ---->  0.8
---------------------------------------------------
Enter the Base_x number: 0.8
Enter the Radix number: 2

With the Product whole value ---->  1.0
The remainder of  0.8  and  2  is ---->  0.6
---------------------------------------------------
Enter the Base_x number: 0.6
Enter the Radix number: 2

With the Product whole value ---->  1.0
The remainder of  0.6  and  2  is ---->  0.2
---------------------------------------------------
Enter the Base_x number: 0.2
Enter the Radix number: 2

With the Product whole value ---->  0
The remainder of  0.2  and  2  is ---->  0.4
---------------------------------------------------
Enter the Base_x number: 0.4
Enter the Radix number: 2

With the Product whole value ---->  0
The remainder of  0.4  and  2  is ---->  0.8
---------------------------------------------------
Enter the Base_x number: 0.8
Enter the Radix number: 2

With the Product whole value ---->  1.0
The remainder of  0.8  and  2  is ---->  0.6
---------------------------------------------------
Enter the Base_x number:
```
### Interpretation of the example run:
- In the example shown, the user is prompted with a *Base_x* value and *Radix* value. In the following example, the *Base_x* value that was chosen was **0.35** and the *Radix* is **2**. The interpretation of this is that we are converting the decimal (base 10) value of 0.35 the binary representation using base 2 (Radix value). For this example, the first 8 bits of the Binary representation is found.
- Each run of the program will produce an *'Product whole value'* value and a *remainder* value. 
    - The *'Product whole value'* value is the value that will be used to write the Binary representation of a decimal value.
    - The *remainder* value is used as the new *Base_x* to continuously multiply by the *Radix* value.
- When interpreting the result, the *Product whole value* values will be read from top (Lease Significant Bit) bottom (Most Significant Bit). In the example case, it will be read as the following:
    - 01011001
        - This will be written as .01011001
    - The following result shown, demonstrates the Binary representation of the original decimal value of the Decimal number 0.35.