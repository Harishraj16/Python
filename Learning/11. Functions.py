# Fuctions in python

'''
def welcome():
    print("Welcome to my teritory")
    
    
welcome()
'''

#No Return Type Without Argument Function

'''
def add():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    c=a+b;
    print("Total =", c)
    
add()
'''

#No Return Type but With Argument Function

'''
def sub(a,b):
    c=a-b 
    print('Difference: ',c)
    
sub(25,2)
'''

#Return Type without Argument Function

'''
def mul():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    c=a*b
    return c
    
x=mul()
print("Multiplication answer:",x)

'''


#Return Type With Argument Function

'''
def div(a,b):
    c=a/b 
    return c
    
x=div(25,2)
print("Quotient:",x)

'''

#Arbitary Argument Function

'''
# Definition

An arbitrary argument function in Python allows you to pass
a variable number of arguments to a function.
'''

'''
def class_10(*students):
    print(students)
    for user in students:
        print(user)
    
class_10("Harish","Lokesh","Vetri","mani","Rahmaan")
'''

#Keyword Argument Function


'''
# Definition

A function that allows arguments to be passed using parameter 
names, enabling flexibility and clarity in argument assignment.

'''

'''
def message(name,age):
    print(name,"age is",age)
    
message(19,"Harish") 
#this prints(19 age is harish) to overcome this we use Keyword Argument

message(age="19", name="Harish")
'''

#Arbitary Keyword Arguments Function

'''
# Definition

A function parameter that collects unspecified keyword arguments into 
a dictionary, allowing for the handling of variable and named inputs.

'''

'''
def biodata(**data):
    print(data)
    
    
biodata(name="Harish",age="19",gender="Male")
'''

#Default Parameter Function

'''
# Definition

A function with parameters that have predefined default values, 
allowing those parameters to be omitted when the function is called.

'''


'''
def user(name,city="Salem"):
    print(name,"is from",city)
    
    
user("Harish","kallakurichi")
user("Viknesh")

'''

#Passing a List as an Argument in Function 

'''
def total(marks):
    return sum(marks)

print(total([55,75,80,95,47]))

'''

#Recursion Function

'''
def factorial(x):
    if x==1:
        return 1 
    else:
        return (x * factorial(x-1))
    
print("Factorial:",factorial(5))

'''

#Lambda Function 

'''
# Definition

An anonymous function created using the lambda keyword, 
often used for short, inline operations without the need for a 
formal function definition.

'''

'''
c=lambda a:a+50
print(c(5))

c=lambda a,b: a*b

print(c(10,15))

'''
