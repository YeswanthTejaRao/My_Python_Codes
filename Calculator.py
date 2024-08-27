# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:36:32 2024

@author: ytejagiduthuri
"""


def operators(n1, n2, operator):
    n1 = float(n1)
    n2 = float(n2)
    result = ""
    if operator == '*':
        #value = n1 * n2
        result = n1 * n2
    #f'{n1} * {n2} = {value}'
    
    elif operator == '+':
        #value = n1 + n2
        result = n1 + n2
    #f'{n1} + {n2} = {value}'

    elif operator == '-':
        #value = n1 - n2
        result = n1 - n2
    #f'{n1} - {n2} = {value}'
        
    elif operator == '/':
        #value = n1 / n2
        result = n1 / n2
    return result
    #f'{n1} / {n2} = {value}' 
    #print(value)  
    
    

last_value = True

def calculator():
    Re_Calcaulation =True
    First_input_number = float(input("What's the First Number? : "))


    while Re_Calcaulation: 
            
        print("*\n+\n-\n/\n")
        operator = input("Pick an operator : ")
        Next_Input_Number = float(input("What's the next Number : "))
        output = operators(First_input_number,Next_Input_Number ,operator)
    
        print(f"{First_input_number} {operator} {Next_Input_Number} = {output}")
        inputt = input(f"Type 'Y' to continue calculationg with {output}, or type 'N' to to start a new calculation ")
    
        if inputt.lower() == 'y':
            First_input_number = output
        else:
            Re_Calcaulation = False
            print("\n" * 100)
            calculator()

calculator()
            


