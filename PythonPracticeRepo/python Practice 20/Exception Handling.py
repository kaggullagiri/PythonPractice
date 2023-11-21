 # Error : interuptng the normal execution of code
 # Error handling : how we can handle the error is called error handling
''' Types of Errors :
  1.syntax error : mistakes in syntax  [ ex: prnt(i)]
  2.logical error : Mistakes in logic [ a=0 ,b=2,a>b ]
  3.Runtime error : * occurs at during the execution of program 
                    * it is also called exception
                     Ex : 11---
                          22---
                          33---
                          44---
                          bnhg--- [here one exception is raised]
            # then remaining lines of code is not executed 
                          666--
                          777---'''
#Exception Handling :

'''1.try - try contains list of statments that may raise an exception or try to find the exception 
 2.Except - Except block contains list of statemnets which handle the exception
 3.else - if exception is not occured then else block will get executed
 4.Finally - Finally block definetly gets executed 
  
   (try,Except,finally are keywords in 35 keywords) '''


def error_handling(n):
    m = 6
    try:
        print(v)
    except:
        print('One exception is arised ')
    else:
        print('no error is occured')
    finally:
        print('code is completed with * error_handling * user defined function')

error_handling(4)
c=error_handling(5)
print(c)
