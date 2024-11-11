# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:07:43 2024

@author: ytejagiduthuri
"""

######## BMI Calculator

def BMI_Cal(a,b):
    result=a/(b**2)
    return result


Weight=float(input("Enter Yur weight in Kg's? "))
Height=float(input("Enter Yur weight in Inches? "))
print(BMI_Cal(Weight,Height))




###### Age Calculator
def Age_Left(Age,Age_Max):
    #Age_Max=90
    final=(Age_Max-Age)*52
    final_string=f"You have {final} weeks left"
    return final_string

Age=int(input("Enter Your Age. "))
Age_Max=90
print(Age_Left(Age,Age_Max))





###### Tip Calculator


print("Welcome to the Tip Calculator")

def tip_calculator(a,b,c):
    Tip_value=a*(b/100)
    Final_amount=round(((Tip_value+a)/c),2)
    re=f"Each Person Should pay $ {Final_amount}"
    return re
    
total_bil=float(input("What was the Total Bill? $\n"))
tip=int(input("How much Tip would you like to give? 10, 12, or 15?\n"))
bill_split_numbers=int(input("How Many members to split the bill?\n"))
print(tip_calculator(total_bil, tip,bill_split_numbers))