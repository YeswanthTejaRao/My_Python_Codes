# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:14:26 2024

@author: Yeswanth
"""

import random

Food=['prawns','gobi','pakodi','sandwich']
IceCream_Flavours=['pista','mango','almond','nuts']
Airline_Company=['emirates','boeing','airbus']

Type_of_Product=['Food','IceCream_Flavours','Airline_Company']
Product_Choice=random.choice(Type_of_Product)
print(f'The Secrect word is related to this Category---->  "{Product_Choice}"\n')
Product_Choice_Dict={"Food":Food,"IceCream_Flavours":IceCream_Flavours,"Airline_Company":Airline_Company}
#print(Product_Choice_Dict[Product_Choice])

word=Product_Choice_Dict[Product_Choice]


"""
w2=""
for i in word:
    #print(i)
    w2+=i
#print(list(w2))
word_list=list(w2)
print(word_list)"""
#print("20================",word_list)


random_word=random.choice(word)
#print(random_word)
w2=""
for i in random_word:
    #print(i)
    w2+=i
#print(list(w2))
word_list=list(w2)
#print(word_list)

random_word_length=len(random_word)

Guess_word_List=[0 for x in range(len(random_word))]
Gues_word_Lenght=[]
Guess_word_String=""

print(f"It's a {random_word_length} Length Secret Word\n")

 
for i in range(0,len(random_word)+2):
    chances=random_word_length+2 - (i+1)
    #print("Chances---------",chances)
    if chances>0:
        if Guess_word_List==word_list:
            #print("Hurray! You got the word!!")
            break
        elif Guess_word_List!=word_list:
            
    
                
            print(f'Number of chances left for you to guess the Word:  "{chances}"\n')
            guess_word=input("Enter Your Input Charcater: ").lower()
            
            if chances>0:
                
                if guess_word in list(random_word):
                    #print(random_word.index(guess_word))
                    Guess_word_List[random_word.index(guess_word)]=guess_word
                    Guess_word_String+=guess_word
                    print(f'Your guessed characters "{Guess_word_List}"\n')
                    #print("32--------",Guess_word_List)
                    
                    if Guess_word_List==word_list:
                        
                        print(f'\t\tHurray!\n\tYou got the word!\nThe word is "{Guess_word_List}"\n')
                            #f'You Charcater is one of it. Secret Value "{Guess_word_String}"\n\t Keep Trying have "{chances}" Chances to Find it\n')
                        
                    else:
                        print(f'You Charcater is one of it. Guessed word is "{Guess_word_List}"\n')
                        
                else:
                    print(f'Your Guessed Character is not matching. Try other value. Guessed word is "{Guess_word_List}"\n')
    
            else:
                print(f'\t\t\tSorry Mate\n\t\tYou are out of Chances\n\t*********** Game Over ***********\n----> You Guessed Word is "{Guess_word_List}"')
    
        else:
            print("\t\t\tSorry Mate\n\t\tYou are out of Chances\n\t*********** Game Over ***********")
            break
    elif chances==0:
        #print("Line 92--------------",Guess_word_List)
        print(f'This is u r final chance\nNumber of chances left for you to guess the Word:  "{chances}"\n')
        guess_word=input("Enter Your Guessed Charcater ").lower()
        if guess_word in list(random_word):
            #print(random_word.index(guess_word))
            Guess_word_List[random_word.index(guess_word)]=guess_word
            Guess_word_String+=guess_word
        if Guess_word_List==word_list:
            print(f'\t\tHurray!\n\tYou got the word!\nThe word is "{Guess_word_List}"\n')
            break
        else:
            print(f'\t\t\tSorry Mate\n\t\tYou are out of Chances\n\t*********** Game Over ***********\n----> You Guessed Word is "{Guess_word_List}"\n -----> Correc Word is "{word_list}"')
        """
        if Guess_word_List==word_list:
            #print("Hurray! You got the word!!")
            break
        elif Guess_word_List!=word_list:
            
            print(f'This is the number of chances left:  "{chances}"\n')
            guess_word=input("Enter Your Guessed Charcater ").lower()
            
            if chances>0:
                
                if guess_word in list(random_word):
                    #print(random_word.index(guess_word))
                    Guess_word_List[random_word.index(guess_word)]=guess_word
                    Guess_word_String+=guess_word
                    print(f'Your guessed characters "{Guess_word_List}"\n')
                    #print("32--------",Guess_word_List)
                    
                    if Guess_word_List==word_list:
                        
                        print(f'\t\tHurray!\n\tYou got the word!\nThe word is "{Guess_word_List}"\n')
                            #f'You Charcater is one of it. Secret Value "{Guess_word_String}"\n\t Keep Trying have "{chances}" Chances to Find it\n')
                        
                    else:
                        print(f'You Charcater is one of it. Guessed word is "{Guess_word_List}"\n')
                        
                else:
                    print(f'Your Guessed Character is Wrong. Guessed word is "{Guess_word_List}"\n')
    
            else:
                print(f'\t\t\tSorry Mate\n\t\tYou are out of Chances\n\t*********** Game Over ***********\n----> You Guessed Word is "{Guess_word_List}"')
    
        else:
            print("\t\t\tSorry Mate\n\t\tYou are out of Chances\n\t*********** Game Over ***********")
    """
