''' string :
 * string is a collection of individual elements which are enclosed in quotation marks (single line strings -single ,
    double quotes, for multi line strings we use triple quotes .
 * string is immutable
 * string is ordered
 * here indexing and slicing is possible
 * allows duplicate values '''
# Examples :

s1 = 'Good morning'
s2=  " hello "
s3=  '''
         hi
         welcome to india 
         welcome to asia '''
print(s1,s2,s3)

# by using built in methods examples

print(s1.lower())
print(s2.upper())
print(s1.title())
print(s1.swapcase())
print(s1.islower())
print(s2.isupper())
print(s1.isalpha())
print(s2.isalnum())
print(s1.isdigit())
print(s2.isspace())
