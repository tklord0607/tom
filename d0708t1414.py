#!/usr/bin/python3.10.4 <-指用python第幾版來寫的


#增加y/n選項來進行要不要再玩一次猜數字
#使用了def function區塊再加上while
import random
def pg():
    min = 1
    max = 100
    c=0
    t=random.randint(min,max)
    print("====???====\n\n")
        
    while True:
        k=int(input(f"??範圍{min}~~{max}:"))
        c +=1
        if(k == t):
            print(f"Yes,正確:{t}")
            print(f"你共猜了{c}次")
            break
        elif k>t:
            print("小一點")
            max=k-1
        elif k<t:
            print("大一點")
            min=k+1 
            print("NO")
            print(f"你已猜了{c}次")
while(True):
    pg()
    GO= input("再玩一次?(y,n)")
    if not (GO =="y"):
        break
print("GG")
        