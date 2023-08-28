# Tuple in Python

'''
#Definition

Similar to lists but immutable, tuples are ordered collections 
that can store different data types. Once created, their elements 
cannot be changed.
'''

'''
1. Immutable
2. Surrounded By Round Brackets (1,1,5)
'''

a=(1,2.5,True,"Harish")
print(a)
print(type(a))
print(a[1])
print(a[0])
print(a[-1])
print(a[0:2])

b=list(a)
print(b)
b.append("Lokesh")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)
    
if "Harish" in a:
    print("Harish is found")
else:
    print("Not Found")
    
print(len(a))

print("---------------------------------------------------------")

a=(1)
print(type(a))
a=(1,)
print(type(a))

# =============================================================================
# del a      #container a is deleted completely
# print(a)
# =============================================================================

a=(1,2,3,4)
b=(5,6,7,8)
c=a+b
print(c)
print(c.count(5),"time")


a=(1,2,3,4)
b=(5,6,7,8)
c=(a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])

print("---------------------------------------------------------")


x=("Harish",)*5
print(x)

print("---------------------------------------------------------")

a=(1,2,7,4)
print(min(a))
print(max(a))

print("---------------------------------------------------------")