# file handling :
#  * file handling is the process of performing operations on files .
#  * operations are nothing but creating , reading , writing , deleting
'''
 some basic modes  :

r : open a already created file for a read operation
w : open a file that contains some data then it will be replaced with new data(lost old data)
a : open an existing file for adding data (we didnt lost data y bcz of using append)
r+: To read and write data into the file.
w+: To write and read data(truncate)
a+: To append and read data from the file.

'''
# for writing data

f = open('pythontext_file.txt', 'w')
f.write('This is my first textfile\nI need to write in file\n')
f.write('I am a python programmer')
f.close()
print('Successfully data is updated to file !')

# for reading data

f = open('pythontext_file.txt', 'r')
f.read()
f.close()
print(' Successfully read the file data !')

# for adding data

f = open('pythontext_file.txt', 'a')
f.write('Hello python programmer-First time append/adding')
f.write('I am a python programmer')
f.close()
print('Successfully data is updated to file !')

# for writing and reading data (truncate )-previous data is modify

file = open('pythontext_file.txt','w+')
file.write("It is write and read mode\n previous data is this is my first text file\n i need to write in file ")
file.write("Now i modified the already existing data in the file by using w+")
file.close()