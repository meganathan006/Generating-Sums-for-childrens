import random
operator=["+","-","*"]
 
def generate_problem():
    left=random.randint(3,20)
    right=random.randint(3,20)
    oper=random.choice(operator)

    expr=str(left)+" "+oper+" "+str(right)
    ans=eval(expr)
    return expr,ans

for i in range(int(input("Enter how many problems you want : "))):
    expr,ans=generate_problem()
    while True:
        guess=input("Problem No # " + str(i+1) + " : " + expr + " = ")
        if guess==str(ans):
            break

