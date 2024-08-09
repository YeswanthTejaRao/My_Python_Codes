# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:41:19 2024

@author: ytejagiduthuri
"""

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caser(text, shift, encode_or_decode):
    output_text=""
    text_list=list(text)
    for i in range(len(text_list)):
        if text_list[i] not in alphabet:
            output_text+=text_list[i]
        else:
            if encode_or_decode=='decode':
                Final_Value=alphabet.index(text_list[i])-shift
            else:
                Final_Value=alphabet.index(text_list[i])+shift
            print(alphabet[Final_Value])
            Final_Value%=len(alphabet)
            output_text+=alphabet[Final_Value]
    print(f'Here is the {encode_or_decode}d result: {output_text}')
    #return output_text

should_continue=True

while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift_Number=int(input("Type the Shift Number:\n"))
    
    caser(text, shift_Number, direction)
    
    restart = input("Type 'yes' if you want to go again. otherwise type 'no'.\n").lower()
    
    if restart=='no':
        should_continue=False
        print("GoodBye")



"""

def text_encoding(text, shift):
    final_value=""
    text_list=list(text)
    for i in range(len(text_list)):
        #for j in range(len(alphabet)):
            #print(text_list[j])
        hh=alphabet.index(text_list[i])+shift
        hh%=len(alphabet)
        final_value+=alphabet[hh]
    return final_value
    #print(final_value)
        #break


def text_decoding(text, shift):
    final_value=""
    text_list=list(text)
    for i in range(len(text_list)):
        #for j in range(len(alphabet)):
            #print(text_list[j])
        hh=alphabet.index(text_list[i])-shift
        hh%=len(alphabet)
        final_value+=alphabet[hh]
    return final_value
    #print(final_value)
        #break


if direction.lower()=='encode':
    result=text_encoding(text,shift_Number)
    print(f'Here is the encoded result: {result}')
elif direction.lower()=='decode':
    result=text_decoding(text,shift_Number)
    print(f'Here is the decoded result: {result}')
"""
#print(text_encoding(text,shift))