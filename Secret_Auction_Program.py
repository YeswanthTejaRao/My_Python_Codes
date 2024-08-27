# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:03:36 2024

@author: ytejagiduthuri
"""

import os



def highest_Bid_Amount(Bidding_Dictionary):
    winner=""
    highest_bid=0
    for bidder in Bidding_Dictionary:
        Bid_Amount = Bidding_Dictionary[bidder]
        if Bid_Amount > highest_bid:
            highest_bid = Bid_Amount
            winner = bidder
    print(f'The Winner is "{bidder}" with a bid of "{highest_bid}" ')



Bidding_Dictionary={}

Bid_Person = True

while Bid_Person:
    Name_Input = input("What is Your Name? : ")
    Bid_Price = int(input("What's Your Bid Amount : $"))
    Bidding_Dictionary[Name_Input] = Bid_Price
    Others_Bid = input("Are there any Bidders? Type 'Yes' or 'No' \n").upper()
    if Others_Bid == 'NO':
        Bid_Person = False
        highest_Bid_Amount(Bidding_Dictionary)
    elif Others_Bid == 'YES':
         os.system('clear')
         print("\n" * 90)  


