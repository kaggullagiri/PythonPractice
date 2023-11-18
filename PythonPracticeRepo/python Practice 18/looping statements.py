# if we want to execute set of instructions repetaedly until condition satisfy

#1. For loop

 # Examples1 :

s='Giri'
for i in s:
    print(i) # i is dummy value consider individual element

 # Example2 :

l=[11,22,33,44,55]
for i in l:
    print(i)

# Example 3:

t=10,20,30,40
for i in t:
    print(i)

# Example 4:

se={1,2,3,4,5}
for i in se:
    print(i,id(i))

# Example 5:

dic = {'name':'Giri','Id':123}
for i in dic:
    print(i)    # in dictionary only keys will be comes in output

# ex6 : length of string

s='girikola'
l=0
for i in s:
    l=l+1
print(l)

#ex7: count how many times sub string is present

s='girikola'
sub='i'
c=0
for i in s:
    if i==sub:
        c=c+1
print(c)

#ex8 : how many vowels are present in string

s='girikola'
vow='aeiouAEIOU'
c=0
for i in s:
    if i in vow :
        c=c+1
print(c)

#ex9 : how many consonants are in string

s=('girikola')
s1='aeiouAEIOU'
con=0
for i in s:
    if i not in s1:
        con=con+1
print(con)

#ex10: how many digits present in string

s='kaggullagiri124'
d=0
for i in s:
    if i.isdigit():
        d=d+1
print(d)







