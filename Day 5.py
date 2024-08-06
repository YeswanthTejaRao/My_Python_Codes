# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:22:38 2024

@author: ytejagiduthuri
"""

##################### Option 1

import random

Letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Numbers=[0,1,2,3,4,5,6,7,8,9]
Symbols=['@','$','^','&','*','!','$','%','(',')','{','}',';',':','-','+','=','?','>','<']

Final=[]
Final_2=[]
Final_3=[]
Final_PAssword=""

No_Letters=int(input("How many Letters do u want? "))
No_Numbers=int(input("How many Numbers do u want? "))
No_Special=int(input("How many Special Charcaters do u want? "))
#Max_Password_Length=int(input("What is Maximum Password Length? "))

for i in range(0,No_Letters):
    i=random.randint(0, len(Letters)-1)
    Final.append(Letters[i])

for i in range(0,No_Numbers):
    i=random.randint(0, len(Numbers)-1)
    Final_2.append(str(Numbers[i]))

for i in range(0,No_Special):  
    i=random.randint(0, len(Symbols)-1)
    Final_3.append(Symbols[i])

Total=Final+Final_2+Final_3
random.shuffle(Total)

for val in Total:
    Final_PAssword+=val

print(f"Your Final Password is here   {Final_PAssword}")




############### Option 2

import random

Letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Numbers=[0,1,2,3,4,5,6,7,8,9]
Symbols=['@','$','^','&','*','!','$','%','(',')','{','}',';',':','-','+','=','?','>','<']

Final=[]
Final_PAssword=""

No_Letters=int(input("How many Letters do u want? "))
No_Numbers=int(input("How many Numbers do u want? "))
No_Special=int(input("How many Special Charcaters do u want? "))
#Max_Password_Length=int(input("What is Maximum Password Length? "))

for i in range(0,No_Letters):
    i=random.randint(0, len(Letters)-1)
    Final.append(Letters[i])

for i in range(0,No_Numbers):
    i=random.randint(0, len(Numbers)-1)
    Final.append(str(Numbers[i]))

for i in range(0,No_Special):  
    i=random.randint(0, len(Symbols)-1)
    Final.append(Symbols[i])


random.shuffle(Final)

for val in Final:
    Final_PAssword+=val

print(f"Your Final Password is here   {Final_PAssword}")