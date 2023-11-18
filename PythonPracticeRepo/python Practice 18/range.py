# range : providing limits inorder to execute for loop

     #  syn: range(sv,Ev+-1,updation)

#1. Find sum of first n natural numbers

n=10
s=0
for i in range(1,n+1):
    s=s+i
print(s)

#2. factorial of a given number

n=5
f=1
for i in range(1,n+1):
    f=f*i
print(f)

#3. print all even num

n=20
for i in range(1,n+1):
    if i%2==0:
        print(i)

#4.print sum of odd numbers


summ=0
for i in range(20,30+1):
    if i%2!=0:
        summ=summ+i
print(summ)

#5.print index positions and its element of string

s='Giri'
for i in range(len(s)):
    print(i,s[i])

