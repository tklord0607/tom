#!/usr/bin/python3.10.4 <-指用python第幾版來寫的

import random

min = 1
max = 10
c=0
t=random.randint(min,max)
print("====???====\n\n")
#t=random1~10隨機產生，c=0 當k=t時遊戲結束，k由玩家輸入數值
#在while的區塊下 每執行一次c由0+1累計
while True:
    k=int(input(f"??範圍{min}~~{max}:"))
    c +=1
    if(k == t):
        print(f"Yes,正確:{t}")
        print(f"你共猜了{c}次")
        break
    else:
        print("NO")
        print(f"你已猜了{c}次")
print("GG")