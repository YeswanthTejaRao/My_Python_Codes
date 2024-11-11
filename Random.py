# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:25:42 2024

@author: ytejagiduthuri
"""

import random

mm=random.randint(1, 3)
if mm==1:
    print("Heads")
elif mm==2:
    print("Tails")
print(mm)

mm2=random.random()
print(mm2)

mm3=random.uniform(1, 10)
print(mm3)

friends=["Alice",'bob',"Arnold","Tight","Emma","Scarlet"]

# option 1
pick=random.randint(0,len(friends)-1)
print(friends[pick])

# option 2
pick_2=random.choice(friends)
print(pick_2)




##### Rock Paper Scissor

# 0 Rock
# 1 Paper
# 2 Scissor

# Option1 0

#Game=['ROCK','PAPER','SCISSOR']

rand_val=random.randint(0,2)
#rand_val=Input_1[random_num]
print(f"Computer Choice {rand_val}")
Input_1=int(input("Choose Rock, Paper or Scissor "))
print(f"Computer Choice {Input_1}")

if Input_1>=3 or Input_1<0:
    print("You typed invalid Number")
elif Input_1==0 and rand_val==2:
    print("You Win")
elif Input_1==2 and rand_val==0:
    print("You Lose")    
elif Input_1<rand_val:
    print("You Lost!")
elif Input_1>rand_val:
     print("You Win!")   
elif Input_1==rand_val:
    print("It's adraw")







