''' Operators : operators are the elements which are used to perform operation on operands

   # types of operators :

   1.Arithmetic operators
   2.logical operator
   3.Relational operator
   4.Bitwise operator
   5.Assignment operator
   6.Membership operator
   7.Identity operator
   '''

 #  Example 1 : Arithmetic - used for perform mathematical operations

a = 5
b = 30
c = 28

add = a + b

sub = a - b

mul = a * b

normaldivision = b/a

floordivision = c/a

mod = a % b

power = a ** b

print(add)
print(sub)
print(mul)
print(mod)
print(power)
print(normaldivision)
print(floordivision)

# example2: Logical operators (AND,OR,NOT) used for return bool value as output

a = True
b = False
print(a and b)
print(a or b)
print(not a)

# example3 : relational operator / comparision operator (used for getting true or false )

a = 100
b = 200

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#4.Bitwise operator : used to perform operations on the binary value

a = 10
b = 20

print(a & b)
print(a | b)
print(~a,~b)
print(a ^ b)
print(a >> 2)
print(a << 2)

#5.Identity operator : comparing the memory address

s='Giri'
s1='KaggullaGiri'
s2='kola'
print(s is s1)
print(s is not s1)
print(s is s2)

#6.Membership operator : used for checking the element is present or not

x = 20
y = 45
list = [10, 20, 30, 40, 50]


if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")

# assignment operator : used to assign some value to variables


a = 123
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)












