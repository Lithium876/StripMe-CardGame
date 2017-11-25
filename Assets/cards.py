import random

# create a deck of 52 cards
def new_Deck():
    suits=["H","C","S","D"]
    facevalue=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    deck=[]
    for i in range(0,52):
        deck.append([])
    k=0    
    for i in range(0,4):
        for j in range(0,13):
            deck[k]=(suits[i],facevalue[j])
            k+=1
    return deck
