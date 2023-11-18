# if we dont know how many times we have to iterate
 #Ex1: sum of individual elemenst

n=1234
dummy=n
summ=0
while dummy>0:
    r=dummy%10
    summ +=r
    dummy=dummy//10
print(summ)

#ex2: factorial of  number

n=5
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)

#ex3: index positions and elements

s='Girikola'
i=0
while i<len(s):
    print(i,s[i])
    i+=1

#ex4: check prime or not

i=2
n=23
if n>1:
    while i<n//2+1:
        if n%i==0:
            print('not prime')
            break
        i+=1
    else:
        print('prime')
else:
    print('not prime')

#ex5: print 1 to 10
i=1
while i<11:
    print(i)
    i+=1
else:
    print('i am giri in else  ')







