# LOOP Statements in Python

'''
1. While
2. For
'''

# While loop

'''first 10 Numbers'''

# =============================================================================
# i=1
# while i<=10:
#     print(i)
#     i+=1
# =============================================================================
 
''' 10 Even Numbers'''

# =============================================================================
# i=0
# while i<=20:
#     print(i)
#     i+=2 
# =============================================================================

''' 10 Odd Numbers'''

# =============================================================================
# i=1
# while i<=10:
#     print(i)
#     i+=2
# =============================================================================


# Continue

'''odd number'''

# =============================================================================
# i=1
# while i<20:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# =============================================================================


# Break

''' Break at 6 '''
# =============================================================================
# i=1
# while i<10:
#     if i==6:
#         break
#     print(i)
#     i+=1
# =============================================================================


# Range
# =============================================================================
# print(list(range(5)))
# print(list(range(2,5)))
# print(list(range(0,21,2)))
# print(list(range(1,20,2)))
# =============================================================================


# For Loop

'''for loop using range function'''

# =============================================================================
# for i in range(0,21,2):
#     print(i)
# =============================================================================


# =============================================================================
# for i in range(5):
#     a=int(input("Enter the Number:"))
#     b=int(input("Enter the number:"))
#     print(a+b)
# =============================================================================


# Pattern Printing

# =============================================================================
# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print("")
# =============================================================================

# =============================================================================
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")
# =============================================================================

# =============================================================================
# for i in range(65,70,1):
#     for j in range(65,70,1):
#         print(chr(j),end="")
#     print("")
# =============================================================================


#While Else  

# =============================================================================
# i=1
# while i<=5:
#     print(i)
#     i+=1
# else:
#     print("Loop Completed")
# 
# print("------------------------------------------------------")
#     
# i=1
# while i<=5:
#     if i==3:
#         break
#     print(i)
#     i+=1
# else:
#     print("Loop Completed")
# =============================================================================


# For Else

# =============================================================================
# for i in range(1,5):
#     print(i)
# else:
#     print("For Loop Completed")
#     
# print("---------------------------------------")
# 
# for i in range(1,5):
#     if i==3:
#         break
#     print(i)
#     i+=1
# else:
#     print("For Loop Completed")
# =============================================================================
