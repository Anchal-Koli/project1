import random

def check(comp,user):
    if comp== user:
        return 0
    if (comp== 0 and user==1):
        return-1
    if (comp== 1 and user==2):
        return-1
    if (comp== 2 and user==2):
        return-1
    return 1
comp=random.randint(0,2)
user=int(input("0 for stone, 1 for paper and 2 for scissors.\n  "))

print("you: ",user)
print("Computer: ",comp)

score=check(comp,user)
if(score==0):
    print("Its a draw")
elif(score==-1):
    print("You  lose")
else:
    print("You win")