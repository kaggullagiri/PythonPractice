# class : class is a blue print which is followed by objects / to create objects
'''
* from one class we can create multiple objects
* class keyword is used for creating class
* syn : class <class_name>:
              functions :
                  statements
'''

# object : object is a real world entity which has two characteristics states & behaviour

'''Entity - entity means living or non living things'
 states - states are nothing but properties 
behaviour -behaviour is is nothing but functionality 

Ex:  Bird is one class 
         |
         1.parrot is one object - states/properties are 1.colour  & functionality are 1.Eating
                                                        2.weight                      2.Drinking
                                                        3.height                      3.sleeping
                                                        4.Gender                      4.Flying

         2.crow-- is one object - states/properties are 1.colour  & functionality are 1.Eating
                                                        2.weight                      2.Drinking
                                                        3.height                      3.sleeping
                                                        4.Gender                      4.Flying
'''
# Ex: for creating class & object

class A:
    def summ(self,a,b):
        return a+b
obj=A()
print(obj.summ(2,3))

###################################################################

class bird:
    def parrot(self):
        print('I am parrot in class-bird ')
    def crow(self):
        print('I am crow in class-bird')
obj=bird()
obj.crow()

##############################################################################




