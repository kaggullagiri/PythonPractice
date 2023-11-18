# function is a independent block of code which are defined to perform specific task
# functional approach : it is a process of solcving programming prblms by creating functions
''' advantages :
               1.More code reusability
               2.more code readability
               3.acheive code modularity
               4.easy for code debugging and maintance

 # classification : functions are created by using def keyword
1.Built in functions/pre defined functions - these are the functions created by developers
2.user defined functions - these are the functions created by user based on requirement

  # syntax :
                 def function_name():
                           statemenets '''
#Ex1 :
def add(a,b):
    x=a+b
    return x
#ex2:

def iseven(n):
    if n%2==0:
        return True
    else:
        return False
#ex3:

def evenNumbers(ll,ul):
    for i in range(ll,ul+1):
        if iseven(i):
            print(i)
evenNumbers(1,10)

#ex4 :

def isprime(n):
    if n>1:
        for i in range(1,n//2+1):
            if n%i==0:
                break
        else:
            return n

#ex5:

def prime(ll,ul):
    for j in range(ll,ul+1):
        if isprime(j):
            print(j)
prime(10,30)

# examples :

def add():
    a = 10
    b = 20
    c = a+b
    print(c)
add()
##
def mul(x,y):
    c = x*y
    print(c)
x = int(input("Enter 1 number:"))
y = int(input("Enter 2 number:"))
mul(x,y)
##keywords and arguments
def sum(name,sal):
    print("sal",sal)
    print("name",name)
sum(name="rama",sal=1000)
## It accept so many parameters
def demo(*a):
    print(a)
demo(10,20,30)
##
def sum(x,y):
    c=y-x
    print(c)
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
sum(y,x)

