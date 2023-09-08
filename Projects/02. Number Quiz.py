import random
import time

name = input("Tell your name.. ")
print(f"\nHello, {name}!")
print("I have got a game for you!\n")
    
OPERATORS = ["+","-","*","//","%"]
complexity = input("Compexity (easy/medium/tough): ")

if complexity.lower() == "easy":
    MIN_OPERAND = 1
    MAX_OPERAND = 10
    
elif complexity.lower() == "medium":
    MIN_OPERAND = 1
    MAX_OPERAND = 32
    
elif complexity.lower() == "tough":
    MIN_OPERAND = 30
    MAX_OPERAND = 100

TOTAL_PROBLEMS = int(input("Enter the number of problems: "))

#Generatin the random expression

def generate_problem():
    num1 = random.randint(MIN_OPERAND, MAX_OPERAND)
    num2 = random.randint(MIN_OPERAND, MAX_OPERAND)
    num3 = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator1 = random.choice(OPERATORS)
    operator2 = random.choice(OPERATORS)
    
    if complexity.lower() == "easy":
        expr = str(num1) + " "+ operator1 + " " + str(num2)
        
    elif complexity.lower() == "medium":
        expr = str(num1) + " "+ operator2 + " " + str(num2) + " "+ operator1 + " " + str(num3)
        
    elif complexity.lower() == "tough":
        expr = str(num1) + " "+ operator1 + " " + str(num2) + " "+ operator2 + " " + str(num3)
        
    answer = eval(expr)
    return expr,answer
    
    
input("Press enter to Start!")
start_time = time.time()
print("------------------------------------------------")

for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + "= " )
        if guess == str(answer):
            break
        
        
print("------------------------------------------------")   
end_time = time.time()
total_time_seconds = end_time - start_time 
total_time_minutes = total_time_seconds/60


print("You have completed the quiz in : ", round(total_time_minutes,2) ,end="")
if total_time_minutes <= 1 :
    print(" minute")
else:
    print(" minutes")
    
print("Nice Work!")
    
    