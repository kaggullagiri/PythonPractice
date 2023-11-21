# Inheritance : Inheritance is the process of inherits the properties from parent class to child class

''' * inheritance is the process of deriving properties from main class to sub class '''

# * Types of Inheritance :

# 1.single inheritance : deriving properties from one parent to one child class

# Example :

class parent:
    def fun1(self):
        print('I am parent class')
class child(parent):
    def fun2(self):
        print('Im a child class')
obj=child()
obj.fun2()
obj.fun1()

#2.Multiple inheritance : one child class acquiring properties from multiple parents

class father:
    def fun5(self):
        print( 'i am father')
class mother:
    def fun4(self):
        print( 'i am mother')
class child(father,mother):
    def fun3(self):
        print('hai im child')
obj=child()
obj.fun3()

#3.Multilevel inheritance : one grandparent , one parent,one child
#   * acquring properties from one grand parent after that from parent to child

class Grandfather:
    def fun1(self):
        print('Im grandpa')
class Father(Grandfather):
    def fun2(self):
        print('Im ur father')
class Child(Father):
    def fun3(self):
        print('Im children acquired properties from parent & grandpa')
obj=Father()
obj.fun2()

#4.Heirarchial inheritance: from one parents to two children

class parent:
    def fun1(self):
        print('parent')
class child1(parent):
    def fun2(self):
        print('child1')
class child2(parent):
    def fun3(self):
        print('child2')
obj=child2()
obj.fun3()

##############################################################################
