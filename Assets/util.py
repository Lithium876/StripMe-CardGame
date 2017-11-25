from Assets.ADT import *
from Assets.cards import *

showGreeting = """\
********************************************************
* WELCOME to Strip Me 								                 *
* 													                           *
* Rules of the game: Check the docs 				           *
* 													                           *
* Game Play: 										                       *
* - player 0: the computer 							               *
* - player 1: you 									                   *
* - enter: play the top card and place on discard pile *
* - q: quit i.e. stop playing the game 				         *
* 													                           *
* Enjoy! 											                         *
********************************************************
"""
payCards = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}

def isPayCard(card):
	'''
	Function that determines whether a card is a pay
	card. Name the function isPayCard
	'''
	if card[1] in payCards.keys():
		return True
	else:
		return False
	
def getCardRate(card):
	'''
	Function which accepts a card as its only argument. If the card argument
	is a pay card, it returns its pay rate, otherwise it returns 0
	'''
	if isPayCard(card):
		return payCards.get(card[1])
	else:
		return 0
