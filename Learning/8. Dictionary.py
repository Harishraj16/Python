#Dictionary in python



'''
#Definition

Also known as dicts, dictionaries are collections of key-value pairs.
They allow efficient retrieval of values based on their associated keys.
 
'''


user={
      "name":"Harish",
      "age": 19,
      "isMarried": False
      }

print(user)
print(type(user))

print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

print("\n\ntems in Dictionary: ")
for i in user:
    print(i,":",user[i])
    
print("\n")
for x,y in user.items():
    print(x,y)
    
print("\n\nValues in Dictionary: ")
for i in user.values():
    print(i)
    
print("\n\nKeys in Dictionary: ")
for i in user.keys():
    print(i)
    
    
if "age" in user:
    print("\nPresent")
    
if "gender" in user:
    print("\nPresent")
else:
    print("Not Present")
    
    
    
#Changing Values

user.update({"gender":"male"})
print(user)

user["age"]=25
print(user)

user.pop("age")
print(user)

user.clear()
print(user)

'''
del user
print(user)
'''


print("---------------------------------------------------------------")

#Nested Dictionary

users={
       
       "user1":{
             "name":"Harish",
             "age": 19,
             "isMarried": False
             },
       
       "user2":{
             "name":"Lokesh",
             "age": 35,
             "isMarried": True
             },
       
       "user3":{
             "name":"Nalan",
             "age": 32,
             "isMarried": True
             }
       }

print(users)



    
