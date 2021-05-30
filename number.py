##print("Hello Eason")

import random
print("數字猜迷遊戲")

number = random.randint(1,10)
changes = 0 ##在這邊設定可以猜幾次

print("請猜一個1到10之間的數字,你有5次機會")

##宣告while迴圈來讓迴圈執行
while changes < 5:
    guess = int(input()) ##把輸入的值轉換成int
    
    if guess == number:
        print("你猜對了！！！")
        break
    elif guess < number:
        print("你猜的數字太小了，實際數字比 ", guess," 還要大，請再猜一次")
    
    else:
        print("你猜的數字太大了，實際數字比 ", guess," 還要小，請再猜一次")
    changes += 1

if not changes < 5:
    print("很可惜你沒猜中，答案是", number, " 下次繼續加油")
