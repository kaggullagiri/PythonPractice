# poly - means 'many' , morphism - means 'ways' & same method
 # same method in different ways or different context

 # types of polymorphism :
  # 1.compile time - here method overloading ( same class,same function name ,different arguments)
  # 2.Run time  - here method overriding( different classes ,same functions ,different arguments)

  # example1: for method overriding

class school:
    def maths(self,a,b):
        return a*b
class school1:
    def maths(self,a,b,c):
        return a*b*c
obj1=school()
c=obj1.maths(2,3)
obj2=school1()
d=obj2.maths(2,3,4)
print(c,d)


############################################

#ex2:method over loading

class vehicle:
    def car(self):
        print('morris garrage')
    def car(self):
        print('pulsar')


obj=vehicle()
obj.car()

#################################


