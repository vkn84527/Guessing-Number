import random as rd
import math
attempt=1
money=0
num,val,n1,n2,n3=0,0,0,0,0
def play_game():
    global num,val,n1,n2,n3
    num=rd.randint(100,999)
    val=[int(ch) for ch in str(num)]
    n1=int(input("guess digit for units palce : "))
    n2=int(input("guess digit for tenths palce : "))
    n3=int(input("guess digit for hundread palce : "))
def cheak_val():
    global money,attempt
    if val[0]==n3:
        money+=200
        attempt=0
        print("you won 200")
    if val[1]==n1:
        money+=100
        attempt=0
        print("you won 100")
    if val[2]==n1:
        money+=50
        attempt=0
        print("you won 50")
        
def change_attemp():
    global attempt
    if int(math.fabs(n1-(num%10)))==1:
        attempt+=1
        print("congratulation you win an attempy")
    if int(math.fabs(n2-((num//10)%10))) in [1,2]:
        attempt+=1
        print("congratulation you win an attempy")
    if int(math.fabs(n3-((num//100)%10))) in [1,2,3]:
        attempt+=1
        print("congratulation you win an attempy")
    attempt-=1
    print("remaning attemps  :",attempt)

    
while attempt>0:
    play_game()
    cheak_val()
    change_attemp()
    print("our generated number is : ",num)
    print("your guess is",n3,n2,n1)
    
    if attempt==0:
        print("you won : ",money)
        ch=input("do u want to bet your and get double price (y/n)")
        if ch.lower()=='y':
            play_game()
            if num==int(str(n3)+str(n2)+str(m1)):
                money*=2
                print("congrates you won",money)
            else:
                primnt("fuck off!!!   :):):_)")
                
        break
    
    
