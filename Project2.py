import random
import time

Operators = ["+","-","*"]
min_operator = 3
max_operator = 12
total_problems = 5

def generate_problem():
    left = random.randint(min_operator,max_operator)
    right = random.randint(min_operator,max_operator)
    operator = random.choice(Operators)
    
    exp = str(left) + " " + operator + " " + str(right)
    result = eval(exp)
    return exp, result

print("Press enter to start")
print("--------------------")

start = time.time()

for i in range(total_problems):
    exp, answer =  generate_problem()
    while True:
        user_answer = input("Problem #" + str(i+1) + ":" + exp + " = ")
        if(user_answer == str(answer)):
            break

end = time.time()

print("--------------------")
print("Great! it took you "+str(round((end-start),2))+" seconds.")