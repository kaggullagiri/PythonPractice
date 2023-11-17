# local variable : created inside a variable and used inside a function
#example1:
place1 = 'bangalore'
def where_are_you():
    place2 = 'office'
    print('Im in ' + place1 + ' at ' + place2 )
where_are_you()

#example2 :

def How_are_you():
    f='Fine'
    print('Im ' + f )
How_are_you()
