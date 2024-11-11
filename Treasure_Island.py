# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:39:13 2024

@author: ytejagiduthuri
"""

print("Welcome to the Treasure Island.\nYour mission is to find the treaure")

print('You are at cross road. Where do you want to go?\n\t\tType "left" or "right"')
input_1=input()

if input_1.upper()=='RIGHT':
    print("Fall in(to a Hole\n Game Over :)")
elif input_1.upper()=='LEFT':
    print("Type Swim or Wait")
    input_2=input()
    input_2=input_2.upper()
    if input_2=='SWIM':
        print("Attacked by trout\n Game Over :)")
    elif input_2=='WAIT':
        print('you Landed on the Floor.\nPlease choose a door "Red" , "Blue" , "Yellow"')
        input_3=input()
        input_3=input_3.upper()
        if input_3=='RED':
            print("Burned By fire\n\t\tGame Over :)")
        elif input_3=='BLUE':
            print("Eaten by beasts\n\t\tGame Over :)")
        elif input_3=='YELLOW':
            print("Hurray You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Fall in(to a Hole\n Game Over :)")
    