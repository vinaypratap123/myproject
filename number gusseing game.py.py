import random
num=random.randint(1,50)
k=1
count=0
score=0

while k:
    i=1
    
  
    while i<6:
        
        print("guess any number")
        n=int(input())
        if n==num:
            score=score+1
            print("congratulation! you won the game")
            print("you took",i,"chnace")
            break
        elif n<num:
            print("your number is small")
            print("try again")
            print(5-i,"chance are left\n\n")
            i=i+1
            continue
        else:
            print("your number is big")
            print("try again")
            print(5-i,"chance are left\n\n")
            i=i+1
            continue
    if i==6:
        count=count+1
        print("your score is:",score,"/",count)
        print("you loss the game\n better luck next time")
        print("\ndo you want to continue play............... \n for yes press 1\n for no press 0")
        k=int(input())
    else:
        count=count+1
        print("your score is:",score,"/",count)
        print(" \ndo you want to continue to play............... \n for yes press 1\n for no press 0")
        k=int(input())
        

