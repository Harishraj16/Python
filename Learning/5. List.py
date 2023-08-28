# List in python 

'''
#Definition

An ordered collection in Python that can hold elements of different 
data types and allows for modification of elements. Lists are mutable.

'''

'''
Sequence type
Mutable
'''

a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print("Slicing")
print(a[2])
print(a[-1])
print(a[0:3])
print(a[2:])

print("-----------------------------------------------------")

a=[1,True,"Ram",2.5]
print(a)
print(type(a))
print(a[0],"is type of",type(a[0]))
print(a[1],"is type of",type(a[1]))
print(a[2],"is type of",type(a[2]))
print(a[3],"is type of",type(a[3]))


print("------------------------------------------------------")


a=[1,True,"Ram",2.5,[1,2,3,4]]
print(a)
print(type(a))
print(a[0],"is type of",type(a[0]))
print(a[1],"is type of",type(a[1]))
print(a[2],"is type of",type(a[2]))
print(a[3],"is type of",type(a[3]))
print(a[4],"is type of",type(a[4]))
print(a[4][1])

print("-------------------------------------------------------")


a=[10,25,35,45]
print(a)
a.clear()
print(a)
b=a.copy()
print(b)


print("-------------------------------------------------------")


a=[10,25,35,45,25,4,25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0) #remove element using index value
print(a)     
a=[10,25,35,45,25,4,25]
a.remove(25)
print(a)

print("-------------------------------------------------------")


names1=["Ram"]
names1.append("Harish")
names1.append("Lokesh")
names1.append("Mithun")
names1.append("vetrimaran")
print(names1)

names2=["Sudha","Yamini"]
names1.extend(names2)
print(names1)

names1.insert(0, "Nalan")
print(names1)


print("-------------------------------------------------------")


print(list(range(5)))
print(list("Harish"))  
a=[10,40,70,20,12,48]
a.sort()
print(a)
a.sort(reverse=True)
print(a) 
a=["orange","apple",'zebraas']
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["orange","apple",'zebraas']
a.sort(key=len)  #sorting based on length
print(a)
a.sort(reverse=True)
print(a)

print("-------------------------------------------------------")
