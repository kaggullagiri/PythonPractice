# slicing : Extracting multiple elements from the direction
    # syntax : var[sIp : EIp +- 1: updation]
   #Types : 2 types
  #1. positive slicing : Extracting multiple elements in the direction of left to right
  #2. Negative slicing : Extracting multiple elements in the direction of right to left

   # updation is 1 by default in positive , for negative we need to update definetly

 # string slicing

s='hai python'
p =s[0:-1:1]
q=s[::-1]
print(p)
print(q)


# list slicing

l=[7,5,20,23,31,134]
a=l[1:5:]
b=l[:-4:-1]
print(a,b)

# tuple slicing

t=100,200,300,400,500
c=t[0:3:1]
d=t[-1:-4:-2]
print(c,d)

# in set and dictionary slicing is not possible

