''' it is the process of calling the function with in itself until the condition is satisfied
  adv : for repeating the same ,recursion is best
       * reduces code complexity
 disadv : Memory consumption is high

 syntax:  def recursive Function():
                 statements
                 if condition:
                       termination
                recursive function()
 '''

#ex1:

def display(n):
    print(n)
    if n==7:
        return
    display(n-1)
print(display(10))

#ex2: sum of n numbers

def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))

#ex3: sum of individual digits

def indsum(n):
    if n==0:
        return 0
    return n%10+indsum(n//10)
print(indsum(123465))

#ex4: factorial

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(6))


