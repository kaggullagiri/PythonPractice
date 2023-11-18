# lambda is a anonymous single line function ,it is created when we need some functionality at that particular time

'''  * lambda keyword is used for defining lambda keyword
       * by default lambda function returns output of given expression
        * in this we can write only single statement
        * syntax : lambda arguments : expression '''

#ex1: with one arg

a= lambda x:x*2
print(a(10))

#ex2 : even or not
iseven =lambda n:n%2==0
print(iseven(20))

#ex3: with two arguments

add = lambda x,y:x+y
print(add(12,23))

#ex4:with three arguments

mul=lambda a,b,c:a*b*c
print(mul(10,2,3))

#examples:
## Lamda Functions in python
k = (lambda a,b:a+b)
print(k(10,20))
##
a = (lambda h:h**3)
print(a(2))
  ## or
b = (lambda c:c**3)
print(b(5))
  #or
c = (lambda a,b:a*b+10)
print(c(3,4))
### Filter function
a = [1,3,5,3,2,6,8]
def add(x):
    if x % 2==1:
        return True
    else:
        return False
k = filter(add,a)
print(list(k))
##addition
k = (lambda a,b,c:a+b+c)
print(k(2,3,4))
##subtraction
'''a = int(input("Enter a number"))
b = int(input("Enter a number 2"))
k = (lambda a,b:b-a)
print(k(a,b))'''
##conditional statement in lamda
k =(lambda x: 'Even' if x%2==0 else 'Odd')
print(k(3))
print(k(2))
##filter the even numbers using filter function
a = [1,2,3,4,5,6,7,8,9,10]
x = list(filter(lambda x:x%2==0,a))
print(x)
### filter the positive numbers using filter method
a = [-1,-2,-3,4,5,-6,7]
s = list(filter(lambda a: a > 0,a))
print("positive-",s)
###
a = [1,3,5,3,2,6,8]
def add(x):
    if x % 2==1:
        return True
    else:
        return False
k = filter(add,a)
print(list(k))
##      or
a = [1,3,5,3,2,6,8]
k = list(filter(lambda a: a % 2 == 1 ,a))
print("Odd",list(k))
### divisible by 5 using filter function in lamda functions
a = [5,10,3,4,5,15,25,45,7,8,9]
k = list(filter(lambda a: a%5 == 0,a))
print("These numbers are divisible by 5",k)
## using tuples
a = (5,10,3,4,5,15,25,45,7,8,9)
k = tuple(filter(lambda a: a%5 != 0,a))
print("These numbers are not divisible by 5",k)
###conditional statements in lamda
k = (lambda n: 'Even' if n%2==0 else 'Odd')
print(k(2))
###
a = [1,3,5,3,2,6,8]
def add(x):
    if x % 2==1:
        return True
    else:
        return False
##        OR
k = filter((lambda  x:x%2==1),(1,2,3,4,5,6))
print(list(k))
## 0r
print(list(filter((lambda  x:x%2==1),(1,2,3,4,5,6))))
### leap year using lamda
a = [2012,2014,2018,2020,2024]
k = list(filter(lambda a:a%4==0 or a%400==0 and a%100==0,a))
print(k)
### divisible by 9+
a = [9,18,27,36,45,54]
k = list(filter(lambda a: a%9 == 0 and a<=45,a))
print("These numbers are divisible by 9",k)
#Reduce function
a = [1,3,5]
from functools import reduce
def add(x,y):
    return x+y
k = reduce(add,a)
print(k)
###
from functools import reduce
k = reduce((lambda x,y:x+y),(10,20,30))
print(k)
### divisible by 2 and divisible 3 and sum the result
from functools import reduce
x = [1,2,6,12,24]
k = reduce((lambda x,y:x+y),(list(filter(lambda x:x%2==0 and x%3==0,x))))
print(k)
###
'''x = [1,2,6,12,24]
k = reduce((lambda x,y:x+y),(list(filter(lambda x,y:x<y,x))))
print(k)'''
### map
a = [10,20,30]
def add(x):
    return x+100
k = map(add,a)
print(list(k))
## using lamda of map
a = [10,20,30]
k = (list(map((lambda x:x+100),a)))







