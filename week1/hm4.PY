# بازی عدد شانسی
import random
pc_num=random.randint(1,20)
for i in range(5):
    user_num=int(input('enter gusse number:  '))
    if user_num<pc_num:
        print("enter bige number ")
    elif user_num>pc_num:
        print("enter small number ")
    elif user_num==pc_num:
        print("end game")
        break