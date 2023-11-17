# Given number is More than 100 or not

a = int(input('Enter a number:'))
if a > 100:
    print(a, ' is more than 100')
else:
    print(a, 'is not more than 100')

# 2.maximum among two numbers

a = int(input('Enter a number:'))
b = int(input('Enter b number:'))
if a > b:
    print(a, 'is maximum')
else:
    print(b, 'is maximum')

# 3.Find given number is even or odd

a = int(input('Enter a Number:'))
if a % 2 == 0:
    print(a, 'is Even number')
else:
    print(a, ' is odd number')

# 4.find given string is palindrome or not

a = eval(input('Enter a string:'))
if a == a[::-1]:
    print(a, 'is palindrome')
else:
    print(a, 'is non palindrome')

# 5.find given two strings are anagrams or not

a = eval(input('Enter a string1:'))
b = eval(input('Enter a string2:'))
if sorted(a.upper()) == sorted(b.upper()):
    print(a, b, 'are anagrams')
else:
    print(a, b, 'are not anagrams')

# 6.find given two numbers are anagrams or not

a = int(input('Enter a number:'))
b = int(input('Enter b Number:'))
c = sorted(a)
print(c)
d = sorted(b)
print(d)
if c == d:
    print('a,b are anagrams')
else:
    print('a,b are not anagrams')

# 7.find maximum amoung three numbers

a = int(input('Enter a number:'))
b = int(input('Enter b number:'))
c = int(input('Enter c number:'))
if a > b and a > c:
    print('a is max')
elif b > c:
    print('b is max')
else:
    print('c is max')

# 8.find maximum amoung four numbers

a = int(input('Enter a number:'))
b = int(input('Enter b number:'))
c = int(input('Enter c number:'))
d = int(input('Enter d number:'))
if a > b and a > c and a > d:
    print('a is max')
elif b > c and b > d:
    print('b is max')
elif c > d:
    print('c is max')
else:
    print('d is max')

# 9.find maximum amoung five numbers

a = int(input('Enter a number:'))
b = int(input('Enter b number:'))
c = int(input('Enter c number:'))
d = int(input('Enter d number:'))
e = int(input('Enter e number:'))
if a > b and a > c and a > d and a > e:
    print('a is max')
elif b > c and b > d and b > e:
    print('b is max')
elif c > d and c > e:
    print('c is max')
elif d > e:
    print('d is max')
else:
    print('e is max')

# 10 .find the given year is a leap year or not

a = int(input('Enter a year:'))
if a % 100 == 0 and a % 400 == 0:
    print('a is centurian year and mainly leap year')
elif a % 100 != 0 and a % 4 == 0:
    print('a is non centurian yaer and mainly leap year')
else:
    print('a is a non leap year')

# 11 .find maximum among three numbers using nested if

a = int(input('Enter a number:'))
b = int(input('Enter b number:'))
c = int(input('Enter c number:'))
if a > b:
    if a > c:
        print('a is max')
    else:
        print('c is max')
else:
    if b > c:
        print('b is max')
    else:
        print('c is max')

# 12. find maximum among five numbers using nested if

a = int(input('Enter a number:'))
b = int(input('Enter b number:'))
c = int(input('Enter c number:'))
d = int(input('Enter d number:'))
e = int(input('Enter e number:'))
if a > b:
    if a > c:
        if a > d:
            if a > e:
                print('a is max')
            else:
                print('e is max')
        else:
            if d > e:
                print('d is max')
            else:
                print('e is max')
    else:
        if c > d:
            if c > e:
                print('c is max')
            else:
                print('e is max')
        else:
            if d > e:
                print('d is max')
            else:
                print('e is max')
else:
    if b > c:
        if b > d:
            if b > e:
                print('b is max')
            else:
                print('e is max')
        else:
            if d > e:
                print('d is max')
            else:
                print('e is max')
    else:
        if c > d:
            if c > e:
                print('c is max')
            else:
                print('e is max')
        else:
            if d > e:
                print('d is max')
            else:
                print('e is max')

# 13 .For loop prgm

s = 'Giri'
for i in s:
    print(i, s.upper())
l = [12, 34, 56, 78, 'hai', 78]
for i in l:
    print(i)
t = (12, 34, 56, 35, 'Hai', 6,)
for i in t:
    print(i)
st = {12, 34, 56, 43}
for i in st:
    print(i, id(i))
d = {'name': 'Gk', 'age': 22, 'Gender': 'Male'}
for i in d:
    print(d.keys())

