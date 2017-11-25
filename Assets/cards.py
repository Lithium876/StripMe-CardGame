import random

# generate a random number between 0 and upperlimit
def genKey(upperlimit):
    return (random.randint(0,upperlimit))

# display a full deck of cards with suit icons
def displayDeck(deck):
    def empty_Deck(deck):
        return deck==[]
    def formatCard(card):
        return card[1]+getSuitIcon(card[0])    
    if empty_Deck(deck):
        raise Exception('Cannot display an empty deck of cards')
    else:
        formattedDeck=[formatCard(c) for c in deck]
        print (formattedDeck[:13],'\n',formattedDeck[13:26],'\n',formattedDeck[26:39],'\n', formattedDeck[39:])

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

#use the UNICODE value to display a suit
def getSuitIcon(suit):
    suitIcon={'H':u"\u2665",'C':u"\u2663",'S':u"\u2660",'D':u"\u2666"}
    return suitIcon[suit]

# shuffle repeatedly splits a deck in half, then interleaves the
# two half-decks together, nbrRounds times
def shuffle(nbrRounds,deck):

    #perform a left circular shift of the cards
    def circular_Shift(cards):
        el=cards[0]
        shiftedCards=cards[1:]
        shiftedCards.append(el)
        return shiftedCards

    #perform nbrPositions repeated circular shifts of the cards
    def shift_Cards(nbrPositions,cards):
        if cards!=[]:
            for ctr in range(nbrPositions):
                cards=circular_Shift(cards)
        return cards

    # split takes a deck as input and splits it into two halves
    def split(deck):
        nbrCards = len(deck)
        return (deck[0:int(nbrCards/2)],deck[int(nbrCards/2):])

    # interleave takes a pair of half-decks as input and returns a new deck
    # The new deck contains all the items of the input half-decks,
    # but with their cards shifted a random number of times
    # then repositioned in alternating order
    def interleave(half_decks):
        hd1,hd2 = half_decks
        if hd1 == []:
            return hd2
        elif hd2 == []:
            return hd1
        else:
            hd1,hd2=shift_Cards(genKey(int(len(hd1))),hd1),shift_Cards(genKey(int(len(hd2))),hd2)
            return [hd1[0]]+[hd2[0]] + interleave((hd1[1:],hd2[1:]))
    
    if  nbrRounds==0:
        return deck
    else:
        return shuffle(nbrRounds - 1, interleave(split(deck)))

