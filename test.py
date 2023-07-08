import random

min = 1
max = 100
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
    elif k>t:
        print("小一點")
        max=k-1
    elif k<t:
        print("大一點")
        min=k+1 
        print("NO")
        print(f"你已猜了{c}次")
print("GG")
while True
      Y
