# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:33:33 2024

@author: Yeswanth Giduturi
"""
import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a Number between 1 and 100")
Difficulty_Level = input("Choose a difficulty. Type 'easy' and 'hard: ")

Lucky_Number = random.randint(1, 100)
print(Lucky_Number)

Easy_Level_Chances = 5
Hard_Level_Chances = 5




def check(Difficulty_Level):
    Chances = ""
    if Difficulty_Level.upper() == "EASY":
        Chances = 10
    elif Difficulty_Level.upper() == "HARD":
        Chances = 5
    else:
        print("Choose a difficulty. Type 'easy' and 'hard: ")
    return Chances



def Number_Guess():
    Main_Counter = check(Difficulty_Level)

    for i in range (0,Main_Counter+1):
        Chances = Easy_Level_Chances - i
            
        if Chances > 0:
            print("You have {} attempts remaining to guess the number.".format(Chances))
            Guess_Number = int(input("Make a guess: "))
            Value = Guess_Number - Lucky_Number
            if Value > 0:
                Value =  Value
            else:
                Value = Value * (-1)

            if Guess_Number == Lucky_Number:
                print("You Won")
                break
            else:
                if Guess_Number > Lucky_Number:
                    print("Too High")
                elif Guess_Number < Lucky_Number:
                    print("To Low")
                print("Guess Again...")
        else:
            print("Sorry Mate! You are out of Moves")


print(Number_Guess())
            
    
    