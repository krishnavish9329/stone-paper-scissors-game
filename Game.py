# stone-paper-scissors-game
# using python code


import random
def result(com,you):
    if (com=="s" and you=="s"):
        print("'Stone' and 'Stone' then Draw the Game")
    elif (com=="p" and you=="p"):
        print("'Paper' and 'Paper' then Draw the Game")
    elif (com=="c" and you=="c"):
        print("'Secissor' and 'Secissor' then Draw the Game")
    elif (com=="s" and you=="p"):
        print("'Stone' and 'Paper' is 'Paper' then you win the Game")
    elif (com=="p" and you=="c"):
        print("'Paper' and 'Secissor' is 'Secissor' then you win the Game")
    elif (com=="c" and you=="s"):
        print("'Secissor' and 'Stone' is 'Stone' then you win the Game")
    elif (com=="c" and you=="p"):
        print("'Secissor' and 'Paper' is 'Secissor' then you loss the Game")
    elif (com=="s" and you=="c"):
        print("'Stone' and 'Secissor' is 'Stone' then you loss the Game")
    elif (com=="p" and you=="s"):
        print("'Paper' and 'Stone' is 'Paper' then you loss the Game")
com= random.randint(1,4)
if(com==1):
    com="s" #s=stone
elif(com==2):
    com="p"#p=paper
else:
    com="c"#c=secissor
#print(com)  
print('''           welcome the "'Stone' 'Paper' 'Secissor'" game 
          you have only three chance''')

for i in range(3):
    you=(input("game the stare\nstone(s),paper(p),secissoe(c)\n"))
    #print(you)
    #print(you)
    if(you=="s"or you=="p" or you=="c"):
        result(com,you)
    else:
        print("you choose incorrect word")
    
