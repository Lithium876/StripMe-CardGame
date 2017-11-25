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

def fillHand(queue,lst):
	'''
	Function that accepts a queue and a list of cards as its arguments.
 	It returns the queue argument with the cards from the list of cards 
 	added to the queue
	'''
	for element in lst:
		enqueue(queue,element)
	return queue

def prepPlayers():
	'''
	Function that creates a new deck of cards, shuffles it, and deals 26 cards 
	to each of 2 players. It then fills the players' hands of cards,
	using fillHand, and returns the filled hands as a tuple.
	'''
	Deck = new_Deck()
	shuffledDeck = shuffle(10, Deck)
	player1Hand=fillHand(makeQueue(),deal(shuffledDeck,26,1)[0][0])
	player2Hand=fillHand(makeQueue(),deal(shuffledDeck,26,1)[0][0])
	return [player1Hand,player2Hand]

def placeCard(playerHand, discardPile):
	'''
	Function that accepts a player's hand of cards and the discard pile as arguments. 
	It then adds the card at the top of that player's hand and places it at the top 
	of the discard pile. It returns the updated player's hand of cards and the 
	updated discard pile. 
	'''
	push(discardPile,dequeue(playerHand))
	return playerHand, discardPile
