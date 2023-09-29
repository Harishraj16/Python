#Set in Python

'''
1. set is an unordered collection of unique elements.
2. Surrounded By Curly Brackets {1,1,5}
3. Sets are useful for removing duplicates and performing
 mathematical set operations.

'''

'''
names={"Harish","Lokesh","Nalan"}
print(names)
print(type(names))

# Access Values Using For loop
for name in names:
    print(name)
    
#Adding New Element

names.add('kamal')
print(names)

a={'mani','rahman','raaja'}
names.update(a)
print(names)
names.remove('raaja')
print(names)
names.discard('raaja') #checks for raaja in set if not found ignored
print(names)
names.pop()
print(names)

names.clear()
print(names)

# =============================================================================
# del names
# print(names)
# =============================================================================
'''

'''
names={"Harish","Harish","Lokesh","Nalan"}
print(names)
'''

'''
a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
print(c)

a.update(b) #store everything in a
print(a)
'''


a={1,2,3,4,5}
b={5,6,7,8,9}
'''
c=a.intersection(b)
print(c)

a.intersection_update(b) # update the intersection value in 'a' itself
print(a)
'''

'''
c=a.symmetric_difference(b)  #print unique elements of both the set
print(c) 
a.symmetric_difference_update(b)
print(a)
'''

a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.isdisjoint(b)
print(c)

a={1,2,3,4}
b={6,7,8,9}
c=a.isdisjoint(b)
print(c)

a={1,2,3}
b={1,2,3,8,9}
c=a.issubset(b)
print(c)

a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.issuperset(b)
print(c)

a={1,2,3}
b={1,2,3}
c=a.issuperset(b)
print(c)
