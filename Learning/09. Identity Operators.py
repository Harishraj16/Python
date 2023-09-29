# Identity Operators

'''
1. is
2. is not

3.Remember that the identity operators compare 
the memory addresses of the objects, not their values.

4.In most cases, you would use the equality operators (== and !=) 
to compare the values of objects.
'''

a=[1,2]
b=[1,2]
c=a
print(id(a))
print(id(b))
print(id(c))

print("\n")
print(a is c)
print(a is b)
print(a==b)    #checking the values


print("\n")
print(a is not c)
print(a is not b)
print(a != b)  #checking the values
